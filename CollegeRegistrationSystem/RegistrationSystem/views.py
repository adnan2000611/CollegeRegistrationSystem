from django.shortcuts import render
from .models import Student
from django.contrib import messages

# Create your views here.
def index(request):

    return render(request , 'loginPage.html')

def home(request):
    return render(request, 'index.html')


def loginpage(request):
    if request.method=="POST":
        try:
            Studentdetails=Student.objects.get(StudentID = request.POST['StudentID'], Password =request.POST['Password'])
            print("Student=", Studentdetails)
            request.session['StudentID']=Studentdetails.StudentID
            return render(request, 'index.html')
        except Student.DoesNotExist as e:
            messages.success(request, 'Student ID or password is wrong')
    return render(request , 'loginPage.html')


def profile(request):
    if request.user.authenticated:
        return render(request, 'profile.html')
    else:
        return redirect('/home/')