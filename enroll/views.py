from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseNotFound  
from django.views.decorators.http import require_http_methods
from enroll.models import Employee as csv
from .forms import TeacherForm
import datetime
from django.template import loader
import csv
from .models import Employee
from reportlab.pdfgen import canvas

from sona1 import settings  
from django.core.mail import send_mail


def home(request):
    emp=Employee.objects.all()
    if request.method=="POST":
        tea=TeacherForm(request.POST,request.FILES)
        if tea.is_valid():
            # return HttpResponse("Http Response Method Is=>"+request.method)
            return HttpResponse("Data Saved Successfully !!! Thank you..")
    else:
        tea=TeacherForm()   
    return render(request,'enroll/home.html',{'emp':emp,'tea':tea})

def getfile(request):
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 55)  
    p.drawString(100,700, "Hello, sonam how are you feeling!!!.")  
    p.showPage()  
    p.save()  
    return response 

def mail(request):
    subject="Greetings"
    msg="COngratulations for new married life bro"
    to="hasan.kamaal0072@gmail.com"
    res=send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if (res==1):
        msg="Mail sent Successfully"
    else:
        msg="Msg could'nt send"
    return HttpResponse(msg)