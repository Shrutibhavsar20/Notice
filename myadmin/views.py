from django.shortcuts import render,redirect
from myadmin.models import *
from user.models import *
from django.contrib.auth.models import User
from django.contrib import auth,messages
from datetime import date
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from django.http import HttpResponse
import PyPDF2



def layout(request):
	context = {}
	return render(request,'myadmin/common/layout.html',context)

def dashboard(request):
	context = {}
	return render(request,'myadmin/dashboard.html',context)
#########################################################################

def add_state(request):
    context = {}
    return render(request,'myadmin/add_state.html',context)

def state_store(request):
    mystate_name =  request.POST['state_name']

    #insert
    State.objects.create(state_name=mystate_name)
    return redirect('/myadmin/add_state')

def all_state(request):
    result = State.objects.all()
    context = {'result' : result}
    return render(request,'myadmin/all_state.html',context)

def delete_state(request,id):
    result = State.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/all_state')

def edit_state(request,id):
    result = State.objects.get(pk=id)
    context={'result':result}
    return render(request,'myadmin/edit_state.html',context)

def update_state(request,id):
    mystate_name =  request.POST['state_name']

    data = {
            'state_name':mystate_name
    }

    State.objects.update_or_create(pk=id,defaults=data)
    return redirect('/myadmin/all_state')
 #########################################################################
def add_city(request):
    result=State.objects.all()
    context = {'cities':result}
    return render(request,'myadmin/add_city.html',context)


def store_city(request):
    result=State.objects.all()
    mycity=request.POST['city_name']
    mysid=request.POST['sid']

    City.objects.create(city_name=mycity,state_id=mysid)
    return redirect('/myadmin/add_city')

def all_city(request):
    result = City.objects.all()
    context = {'result' : result}
    return render(request,'myadmin/all_city.html',context)

def delete_city(request,id):
    result = City.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/all_city')

def edit_city(request,id):
    result = City.objects.get(pk=id)
    result1 = State.objects.all()
    context={'result':result,'cities':result1}
    return render(request,'myadmin/edit_city.html',context)

def update_city(request,id):
    result=State.objects.all()
    mycity=request.POST['city_name']
    mysid=request.POST['sid']

    data={
            'city_name':mycity,
            'state_id':mysid,

    }

    City.objects.update_or_create(pk=id,defaults=data)
    return redirect('/myadmin/all_city')
#####################################################################
def add_area(request):
    city= City.objects.all()
    state = State.objects.all()

    context = {'city':city,'state':state}
    return render(request,'myadmin/add_area.html',context)

def store_area(request):
    myarea = request.POST['area_name']
    mycid = request.POST['cid']
    mysid = request.POST['sid']

    Area.objects.create(area_name=myarea,city_id=mycid,state_id=mysid)
    return redirect('/myadmin/add_area')

def all_area(request):
    result = Area.objects.all()
    context = {'result' : result}
    return render(request,'myadmin/all_area.html',context)

def delete_area(request,id):
    result = Area.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/all_area')

def edit_area(request,id):
    result = Area.objects.get(pk=id)
    result1 = City.objects.all()
    result2 = State.objects.all()

    context={'result':result,'result1':result1,'result2':result2}
    return render(request,'myadmin/edit_area.html',context)

def update_area(request,id):
    result=City.objects.all()
    myarea = request.POST['area_name']
    mycid = request.POST['cid']
    mysid = request.POST['sid']

    data={
            'area_name':myarea,
            'city_id':mycid,
            'state_id':mysid

    }
    Area.objects.update_or_create(pk=id,defaults=data)
    return redirect('/myadmin/all_area')

def users(request):
    result = Register.objects.all()
    context = {'result':result}
    return render(request,'myadmin/users.html',context)

def detail_customer(request,id):
    result = Register.objects.get(pk=id)
    context = {'result':result}
    return render(request,'myadmin/detail_customer.html',context)

def verify(request,id):
    #  id = request.session['id']
    #  mystatus = request.POST['status']
     data = {
          'status':'verify'
     }

     Register.objects.update_or_create(pk=id, defaults=data)
     context = {}
     return redirect('/myadmin/users')

def add_notice(request):
    context = {}
    return render(request,'myadmin/add_notice.html',context)

def notice_store(request):
    mytitle = request.POST['title']
    mydescription = request.POST['description']
    mydate = date.today()
    mypdf = request.FILES['pdf']

    #folder store
    mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
    obj = FileSystemStorage(location=mylocation)
    obj.save(mypdf.name, mypdf)

    Notice.objects.create(title=mytitle,description=mydescription,date=mydate,pdf=mypdf.name)
    return redirect('/myadmin/add_notice')

def all_notice(request):
    result = Notice.objects.all()
    context = {'result' : result}
    return render(request,'myadmin/all_notice.html',context)

def notice_delete(request,id):
    result = Notice.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/all_notice')

def notice_edit(request,id):
    result = Notice.objects.get(pk=id)
    context={'result':result}
    return render(request,'myadmin/notice_edit.html',context)

def notice_update(request,id):
    mytitle =  request.POST['title']
    mydescription =  request.POST['description']
    mydate =  date.today()
    mypdf =  request.FILES['pdf']


    data = {
            'title':mytitle,
            'description':mydescription,
            'date':mydate,
            'pdf':mypdf

    }

    mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
    obj = FileSystemStorage(location=mylocation)
    obj.save(mypdf.name, mypdf)

    Notice.objects.update_or_create(pk=id,defaults=data)
    return redirect('/myadmin/all_notice')





def login(request):
    context = {}
    return render(request,'myadmin/login.html',context)

def login_check(request):
    if request.method == 'POST':
        myusername = request.POST.get('username')
        mypassword = request.POST.get('password')

        if not myusername or not mypassword:
            messages.error(request, "Username and password are required.")
            return redirect('/myadmin/login')

        result = auth.authenticate(username=myusername, password=mypassword)
        if result is None:
            messages.error(request, "Invalid Username or Password 🤭")
            return redirect('/myadmin/login')
        else:
            auth.login(request, result)
            return redirect('/myadmin/dashboard')
    else:
        return render(request, 'myadmin/login.html')

def logout(request):
    auth.logout(request)
    return redirect ('/myadmin/login')

def inquiry(request):
    result = Contact.objects.all()
    context = {'result' : result}
    return render(request,'myadmin/inquiry.html',context)









