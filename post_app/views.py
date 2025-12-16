from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from post_app.models import Posts
from post_app.forms import PostsForm

# Create your views here.
def post_list(request):
    template_name = 'post-list.html' #template
    posts = Posts.objects.all() #query com todas as postagens
    context = { #cria context para chamar no template
        'posts': posts
        }
    return render(request, template_name, context) #render


def post_create(request):
    if request.method == 'POST': #para metodo POST
        form = PostsForm(request.POST, request.FILES) #pega infos do form
        if form.is_valid(): # se for valido
            form = form.save(commit=False)
            form.save() #salva

            messages.success(request, 'O post foi criado com sucesso') #mesnsagem 
            return HttpResponseRedirect(reverse('post-list'))
    form = PostsForm()
    return render(request, 'post-form.html', {"form": form})

def post_detail(request, id):
    template_name = 'post-detail.html'
    post = Posts.objects.get(id=id)
    context = { # cria context para chamar no template
        'post': post
    }
    return render(request, template_name, context) # render

def post_update(request, id):
    post = get_object_or_404(Posts, id=id)
    print(post.id)

    form = PostsForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()

        messages.success(request, 'O post foi atualizado com sucesso') #mesnsagem 
        return HttpResponseRedirect(reverse('post-detail', args=[post.id])) #coloque
    return render(request, 'post-form.html', {"form": form}) #neste template

def post_delete(request, id):
    post = Posts.objects.get(id=id)
    if request.method == 'POST':
        post.delete() #deletar
        messages.success(request, 'O post foi deletado com sucesso') #mesnsagem 
        return HttpResponseRedirect(reverse('post-list'))
    return render(request, 'post-delete.html')