from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *

# Create your views here.
def list(request):
    cs = course.objects.all()
    return render(request, 'list.html', {'courses': cs})

class updatelist(UpdateView):
    model = course
    fields = ['name', 'te']
    template_name= 'update.html'
    success_url = reverse_lazy('listcourse')

def search(request):
    search = request.GET.get('id', '')
    cs = course.objects.filter(id__icontains=search)
    return render(request, 'src.html', {'courses': cs})

def searchname(request):
    search = request.GET.get('name', '')
    cs = course.objects.filter(name__icontains=search)
    return render(request, 'srcn.html', {'courses': cs})

class delete(DeleteView):
    model = course
    template_name = 'del.html'
    success_url = reverse_lazy('listcourse')