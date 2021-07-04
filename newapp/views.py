from newapp.models import List
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your viewsd

def login(request):
    if request.method=='POST':
        try:
          
            email=request.POST['email']
            password=request.POST['password']
            logindata=Logindetails.objects.get(username=email,password=password)
            request.session['logdata']=logindata.id
            return redirect('/newapp/index')
        except:
            return render(request, 'login.html',{"msg":"Invalid email or password"})
    else:
        
        return render(request, 'login.html')



def index(request):
    if request.method=='POST':
        content=request.POST['content']
        logid=request.session['logdata']
        contentdata=List(content=content,user_id=logid)
        contentdata.save()
        logid=request.session['logdata']
        data=List.objects.filter(user=logid)  
     
        return redirect('/newapp/index')

    else:
        logid=request.session['logdata']
        data=List.objects.filter(user=logid)      
        return render(request,'index.html', {"data":data})

def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        passwrd=request.POST.get('password')
        mobile=request.POST['mobile']
        login=Logindetails(username=email,password=passwrd)
        login.save()
        signup=Signup(name=name,email=email,mobile=mobile,user=login)
        signup.save()
        return render(request, 'login.html',{"msg":"successfully registerd please login now"})
    else:

        return render(request, 'signup.html')



def new(request):
    data=List.objects.all()
    return render (request, 'new.html',{"data":data})


def delete_post(request, id):
    logid=request.session['logdata']
    data=List.objects.filter(id=id)
    data.delete()
    return redirect("/newapp/index")

def edit_post(request, id):
    if request.method=="POST":
        content=request.POST['content']
        data=List.objects.filter(id=id)
        for d in data:

            d.content=content
            d.save()
        return redirect("/newapp/index")
    else:
        data=List.objects.filter(id=id)
        return render(request, 'edit.html',{"data":data})
