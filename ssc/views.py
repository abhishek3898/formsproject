from os import supports_bytes_environ
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render                                          
from django.urls import reverse_lazy
from .models import StudentReg                                          
# from .forms import NameForm
from django.views import View                                              
# Create your views here.

def index_page(request):
    students = StudentReg.objects.all()
    return render(request,'index.html',{"students":students})

def new_js(request):
    return render(request, 'js.html')
        
def form_page(request):
    
    if request.method=='POST':
        fn=request.POST.get('name')
        ln=request.POST.get('lastname')
        em=request.POST.get('email')
        ps=request.POST.get('password') 
        ad=request.POST.get('address')
        reg=StudentReg(name=fn,lastname=ln,email=em,password=ps,address=ad)
        reg.save()
        return redirect('detail_page', id=reg.id)
    else:
        return render(request,'form.html')

def details(request, id):
    student = StudentReg.objects.get(id=id)
    context = {"obj":student}
    return render(request, "detail.html", context)

def edit_page(request, id): 
    student = StudentReg.objects.get(id=id)
    context = {"obj":student}
    if request.method == "POST":
        fn=request.POST.get('name')
        ln=request.POST.get('lastname')
        em=request.POST.get('email')
        ad=request.POST.get('address')
        student.name= fn
        student.lastname=ln
        student.email=em
        student.address = ad
        student.save()
        return redirect('detail_page', id=student.id)

    return render(request,'edit.html', context)
    
def delete_page(request, id):
    students=StudentReg.objects.all()
    student = StudentReg.objects.get(id=id)
    context = {"students":students}
    if request.method=="POST":
        student.delete()
        return render(request,'index.html',context)
    return render(request,'delete.html',{"obj":student})
        
    
