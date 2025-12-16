from django import forms
from .models import Posts

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts # nosso modelo
        fields = ['title', 'description', 'image'] #campos do nosso modelo, poderia ser '__all__'

## Tratando estilo em Python
    def __init__(self, *args, **Kwargs ):
        super().__init__(*args, **Kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'