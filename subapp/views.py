from django.shortcuts import render
from . models import student
from django.shortcuts import redirect


def create(request):
    if request.method == "POST":
        t = request.POST.get('title')
        s = request.POST.get('summary')
        y = request.POST.get('year')

        # Save new record
        student.objects.create(title=t, summary=s, year=y)

        # Redirect to list page after saving
        return redirect('list')

    return render(request, 'create.html')


def view(request):
    s=student.objects.all()
    print(s)
    return render(request,'view.html',{'s':s})

def list(request):
    s=student.objects.all()
    return render(request,'list.html',{'s':s})

from django.shortcuts import render, redirect, get_object_or_404
from .models import student

def edit(request, pk):
    e = get_object_or_404(student, pk=pk)

    if request.method == "POST":
        e.title = request.POST.get('title')
        e.summary = request.POST.get('summary')
        e.year = request.POST.get('year')
        e.save()

        # Redirect back to list after update
        return redirect('list')

    return render(request, 'edit.html', {'s': e})



def delete(request,pk):
    d=student.objects.get(pk=pk)
    d.delete()
    s=student.objects.all()
    return redirect('list')
