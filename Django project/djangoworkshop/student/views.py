from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import student_data

def students(request):
    mystudents=student_data.objects.all().values()
    template = loader.get_template('all_students.html')
    #another method for reder function
    '''context={
      'mystudents':mystudents
    }'''
    #render(context,request)
    return HttpResponse(template.render({'mystudents': mystudents}, request))



def home(request):
    mystudents=student_data.objects.all()
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        gender=request.POST.get('gender')

        student_data.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender=gender 
        )
        return HttpResponse("data added successfully. <a herf='/first>Go Back<\a>")
    return render(request,'form.html',{'mystudents':mystudents})