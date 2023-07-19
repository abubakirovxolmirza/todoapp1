from django.forms import ModelForm, DateTimeInput

from .models import Todo


class AddToDo(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'link', 'end', ]
        widgets = {
            'end': DateTimeInput(attrs={'type': 'datetime-local'})
        }