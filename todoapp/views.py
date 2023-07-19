from django.shortcuts import render, redirect, get_object_or_404
import qrcode, os

from ToDo.settings import BASE_DIR
from .models import Todo
from .forms import AddToDo
from django.conf import settings


# Create your views here.
def index(request):
    todo_list = Todo.objects.all()
    return render(request, 'todoapp/index.html', {'todos': todo_list})


def create_todo(request):
    if request.method == 'POST':
        form = AddToDo(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.link = form.cleaned_data['link']
            todo.save()
            qr_data = todo.link
            file_name = f"qrcode_{todo.id}.png"
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            generate_qrcode(qr_data, file_path)
            return redirect('index')
    else:
        form = AddToDo()

    context = {
        'form': form
    }
    return render(request, 'todoapp/add.html', context)


def generate_qrcode(data, file_path):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(file_path)
