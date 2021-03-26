from django.shortcuts import render
import datetime
from django.http import HttpResponse, Http404
from DjangoApp.models import formreg

def index(request):
    return HttpResponse('Hello World ! This is Django Project !')

def getname(request):
    str1=input()
    html="<html> Hello  %s </html>" %str1
    return HttpResponse(html);

def resume(request):
    data={
          "name":"Arul Prasath V",
          "email":"arulprasathv.18cse@kongu.edu",
          "phone":"9994198353",
          "date":datetime.datetime.now(),
          "college":"Kongu Engineering College",
          "course":"B.E CSE"
   }

    return render(request,"resume.html",data)

def hours_ahead(request, offset):
    try:
     offset = int(offset)
    except ValueError:
     raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(days=offset)
    data={"count":offset,
          "datetime":dt
          }
    return render(request,"Datetime.html",data)

def age(request):
    currentDate = datetime.datetime.now()
    deadline = '03/15/2001'
    deadlineDate = datetime.datetime.strptime(deadline, '%m/%d/%Y')
    print(deadlineDate)
    daysLeft = currentDate - deadlineDate
    years = ((daysLeft.total_seconds()) / (365.242 * 24 * 3600))
    yearsInt = int(years)
    months = (years - yearsInt) * 12
    monthsInt = int(months)
    days = (months - monthsInt) * (365.242 / 12)
    daysInt = int(days)
    hours = (days - daysInt) * 24
    hoursInt = int(hours)
    minutes = (hours - hoursInt) * 60
    minutesInt = int(minutes)
    seconds = (minutes - minutesInt) * 60
    secondsInt = int(seconds)
    str1='You are '+str(yearsInt)+ 'years, '+str(monthsInt)+'  months, '+str(daysInt)+'  days, '+str(hoursInt)+'  hours, '+str(minutesInt)+' \
     minutes, '+str(secondsInt)+' seconds old.'
    map={
        "age":str1,
        "dob":"15/03/2001",
        "cur":currentDate
    }
    return render(request, "Datetime.html", map)


def form(request):

    if request.method=='POST':
        formdata = formreg()
        fname=request.POST['fname']
        lname = request.POST['lname']
        roll = request.POST['roll']
        email = request.POST['email']
        phone=request.POST['phone']
        dept = request.POST['dept']
        batch = request.POST['batch']
        sec = request.POST['sec']

        str ="Registration Sucessfull "+fname;
        # str="Name :"+name+" Email  : "+email+" password  : "+password
        formdata.fname=fname
        formdata.lname = lname
        formdata.roll = roll
        formdata.email = email
        formdata.phone = phone
        formdata.roll = roll
        formdata.dept = dept
        formdata.batch = batch
        formdata.sec = sec

        formdata.save()
        return HttpResponse(str)

    return render(request,"FormReg.html")