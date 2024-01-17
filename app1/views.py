from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Data_forms
from .models import Data
import os
def index(request):
  return HttpResponse("hello")

def create(request):
  if request.method=="POST":
    form=Data_forms(request.POST,request.FILES)
    if form.is_valid():
      form.save()
    return redirect('read')
  else:
    form=Data_forms()
  return render(request,'create.html',{'form':form})
# Create your views here.

def retrive(request):
  if request.method=="GET":
    data=Data.objects.all()
  return render(request,'retrive.html',{'data':data})


def update(request,id):
  identity=Data.objects.get(ids=id)
  if request.method=="POST":

    # identity=Data.objects.get(isinstance=identity)
    form = Data_forms(request.POST,request.FILES,instance=identity)
    if form.is_valid():
      if identity.image:
        var_img=identity.image.path
        if os.path.exists(var_img):
          os.remove(var_img)
      form.save()
    return redirect('read')
  else:
    form=Data_forms(instance=identity)
  return render(request,'update.html',{'form':form,'identity':identity})

def delete(request,id):
  identity=Data.objects.get(ids=id)
  identity.delete()
  return redirect('read')

def sure_delete(request,id):
  idd=Data.objects.get(ids=id)
  return render(request,"sure_delete.html",{'idd':idd})


def view_persional_detail(request,id):
  idd=Data.objects.get(ids=id)
  return render(request,'view_persional_detail.html',{'idd':idd})




