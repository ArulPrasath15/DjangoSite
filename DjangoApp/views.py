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
        roll = request.POST['roll']
        data = formdata.__class__.objects.filter(roll=roll).values()
        # print(name)
        if(data.exists()):
            map={"error":"Roll Number Already Registered ! "}
            return render(request,"FormReg.html",map)

        else:
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            phone = request.POST['phone']
            dept = request.POST['dept']
            batch = request.POST['batch']
            sec = request.POST['sec']
            str = "Registration Sucessfull " + fname;
            # str="Name :"+name+" Email  : "+email+" password  : "+password
            formdata.fname = fname
            formdata.lname = lname
            formdata.roll = roll
            formdata.email = email
            formdata.phone = phone
            formdata.roll = roll
            formdata.dept = dept
            formdata.batch = batch
            formdata.sec = sec
            formdata.save()
            return HttpResponse("Registered Successfully "+roll);

    return render(request,"FormReg.html")

def search(request):
    if request.method=='POST':
        formdata = formreg()
        roll = request.POST['roll']
        data = formdata.__class__.objects.filter(roll=roll).values()
        # print(data)
        if(data.exists()):
            # map = {"error": "Roll Number Not Found! "}
            return HttpResponse(data);
        else:
            map = {"error": "Roll Number Not Found! "}
            return render(request, "search.html", map)

    return render(request,"search.html")


def update(request):
    if request.method=='POST':
        formdata = formreg()
        roll = request.POST['roll']
        data=formdata.__class__.objects.filter(roll=roll).values()
        if(request.POST['fname']==''):
            if (data.exists()):
                # print(data)
                list_result = [entry for entry in data]
                # print(list_result[0]['id'])# converts ValuesQuerySet into Python list
                data1 = {
                    "fname": list_result[0]['fname'],
                    "lname": list_result[0]['lname'],
                    "roll": list_result[0]['roll'],
                    "email": list_result[0]['email'],
                    "phone": list_result[0]['phone'],
                    "dept": list_result[0]['dept'],
                    "batch": list_result[0]['batch'],
                    "sec": list_result[0]['sec'],
                    # "fname":list_result[0]['fname'],
                }
                return render(request, "update.html", data1)
            else:
                map = {"error": "Roll Number Not Found! "}
                return render(request, "search.html", map);
        else:
            data=formdata.__class__.objects.filter(roll=roll).delete()
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            phone = request.POST['phone']
            dept = request.POST['dept']
            batch = request.POST['batch']
            sec = request.POST['sec']
            str = " Updated Succesfully " + roll;
            # str="Name :"+name+" Email  : "+email+" password  : "+password
            formdata.fname = fname
            formdata.lname = lname
            formdata.roll = roll
            formdata.email = email
            formdata.phone = phone
            formdata.roll = roll
            formdata.dept = dept
            formdata.batch = batch
            formdata.sec = sec
            formdata.save()
            return HttpResponse(str);

    return render(request,"search1.html")

# def insert(request):
#     error = []
#     formdata = formreg()
#     if request.method == "POST":
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         print(fname, lname, email, phone)
#         if '@' not in email:
#             error.append(" email should have @ ")
#         else:
#             ins = formdata(fname=fname, lname=lname, email=email, phone=phone)
#             ins.save()
#             print("Data saved sucessfully")
#     return render(request, 'insert.html', {'error': error})
#
#
# def search(request):
#     error = []
#     formdata = formreg()
#     if 'fname' in request.GET:
#         q = request.GET['fname']
#     if not q:
#         error.append("Enter a search term ( It can not be empty) ")
#     elif len(q) > 3:
#         error.append(" length can not be greater than 40")
#     else:
#         name = formdata.objects.filter(fname=q).values()
#         print("fname...", name)
#         return render(request, 'search_result.html', {'names': name, 'query': q})
#
#     return render(request, 'search_form1.html', {'error': error})
#
#     # validating fname field and email


'''
def search(request):
    error = []
    if 'fname' in request.GET and 'email' in request.GET:
        q = request.GET['fname']
        mail=request.GET['email']
    if not q:
        error.append("Enter a search term ( It can not be empty) ")
    elif len(q) > 3:
        error.append(" length can not be greater than 40") 
    elif ’@’ not in mail:
        error.append("Wrong Mail ID no @ ")
    else:
        name = formcontact.objects.filter(fname=q).values()
        print("fname...",name)
        return render(request, 'search_result.html', {'names': name, 'query': q})
    return render(request, 'search_form1.html', {'error': error})   

'''


# def search_form1(request):
#     return render(request, 'search_form1.html')
#
#
# def search_form(request):
#     return render(request, 'search_form.html')