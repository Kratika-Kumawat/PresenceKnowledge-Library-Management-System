import re
from django.shortcuts import render,redirect,get_object_or_404
from .models import Student,Library
from django.contrib import messages
from .forms import AddBookForm

def main(request):
    a=Library.objects.all()
    return render(request,'main.html',{'lib':a})

def addstudent(request):
    if request.method == 'POST':
        s=Student()
        s.name=request.POST['name']
        s.enroll=request.POST['enroll']
        s.branch=request.POST['branch']
        s.sem=request.POST['sem']
        s.year=request.POST['year']
        s.mob=request.POST['mob']
        s.save()
        messages.success(request,"Student Added Successfully")
        return redirect('/')
    else:
        return render(request,'addstudent.html')
    
def addbook(request):
    if request.method == 'POST':
        l=Library()
        l.book=request.POST['book']
        l.category=request.POST['category']
        l.language=request.POST['language']
        l.description=request.POST['description']
        l.publisher=request.POST['publisher']
        l.paperback=request.POST['paperback']
        l.save()
        messages.success(request,"Book Added Successfully")
        return redirect('/')
    else:
        return render(request,'addbook.html')

def borrowbook(request,myid):
    obj = get_object_or_404(Library, id=myid)
    form = AddBookForm(request.POST or None ,request.FILES or None ,instance=obj)
    print(form)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "You successfully Borrowed the Book")
        return redirect('/')
    else:
        # messages.success(request, "Something went wrong please try again")
        return render(request,'borrowbook.html' , {'info':form})
    
def studentinfo(request):
    s=Student.objects.all()
    return render(request,'student.html',{'st':s})

def updatebook(request,myid):
    obj = get_object_or_404(Library, id=myid)
    form = AddBookForm(request.POST or None ,request.FILES or None ,instance=obj)
    print(form)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "You successfully Updated the Book")
        return redirect('/')
    else:
        # messages.success(request, "Something went wrong please try again")
        return render(request,'updatebook.html' , {'info':form})
    
def deletebook(request,myid):
    id=int(myid)
    l=Library()
    l.id=id
    l.delete()
    messages.success(request,"Deleted Book Successfully!")
    return redirect("/") 

def delstudent(request,myid):
    myid=int(myid)
    t=Student()
    b=Library.objects.filter(sid_id=myid)
    for i in b:
        i.sid_id=None
        i.save()
    t.id=myid
    t.delete()
    messages.success(request,"You successfully deleted the Student")
    return redirect("/")
    

def info(request,myid):
    l=Library.objects.filter(id=myid).get()
    return render(request,'info.html',{'lib':l})