from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import DOLIST

# Create your views here.
def home(request):
    todo = DOLIST.objects.all()
    if request.method == 'POST':
        new_todo = DOLIST(
            title = request.POST['title'],
            time = request.POST['time']
        )
        new_todo.save()
        return redirect('/')

    return render(request, 'index.html', {'todos': todo})

def delete(request, pk):
    todo = DOLIST.objects.get(id=pk)
    todo.delete()
    return redirect('/')
