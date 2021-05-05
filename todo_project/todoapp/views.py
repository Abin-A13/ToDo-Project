from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from .form import Todoform
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class Tasklist(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task'


class Taskdetails(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task1'


class Taskupate(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'upto'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.id})
class Taskdelete(DeleteView):
    model = Task
    template_name = 'delete.html'
    context_object_name = 'del'
    success_url = reverse_lazy('listview')


def display(request):
    if request.method == "POST":
        na = request.POST.get('task', '')
        pr = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        tas = Task(name=na, priority=pr, date=date)
        tas.save()
    task = Task.objects.all()
    return render(request, "index.html", {'task': task})


# def details(request):
#     task = Task.objects.all()
#     return render(request, "details.html", )

def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request, "delete.html")


def update(request, fid):
    taskh = Task.objects.get(id=fid)
    f = Todoform(request.POST or None, instance=taskh)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, "edit.html", {'fn': f, 'task': taskh})
