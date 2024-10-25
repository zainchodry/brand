from django.http import HttpResponse
from django.shortcuts import render
from pubg.forms import StudentForm
from pubg.models import pubg
def homepage(request):
    stu_form=StudentForm()
    data={
        'form':stu_form
    }
    return render(request,"index.html",data)
def king(request):
    return HttpResponse("zain bhai i love you")
def zain(request,courseid):
    return HttpResponse(courseid)
def save_form(request):
    if request.method=='POST':
        school_name=request.POST['school_name']
        school_place=request.POST['school_place']
        about_school=request.POST['about_school']
        print(school_name,school_place,about_school)
        my_model=pubg(school_name=school_name,school_place=school_place,about_school=about_school)
        my_model.save()
    return HttpResponse("hello world")