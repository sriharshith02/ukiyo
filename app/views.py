from django.shortcuts import render
from django.contrib.auth.models import User,auth
from .models import feed,experience
# Create your views here.
def login(request):
    if(request.method=="POST"):
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if(user is not None):
            auth.login(request,user)
            global current_user
            current_user=username
            return render(request,"index.html")
        else:
            return render(request,"login.html",{'message':'Invalid Credentials'})

    else:
        return render(request,"login.html")
def register(request):
    if(request.method=="POST"):
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if(password1==password2):
            user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name)
            user.save()
            return render(request,"login.html")
    else:
        return render(request,"register.html",{'message':'Passwords not matching'})
def feedback(request):
    if(request.method=="POST"):
        name=request.POST['name']
        rating=request.POST['option']
        fb=request.POST['feedback']
        fed=feed.objects.create(name=name,rating=rating,fb=fb)
        fed.save()
        return render(request,"feedback.html")
    else:
        return render(request,"feedback.html")
def index(request):
    return render(request,"index.html")
def overview(request):
    return render(request,"overview.html")
def deppression(request):
    if(request.method=="POST"):
        name=request.POST['name']
        option=request.POST['option']
        exp=request.POST['feedback']
        ex=experience.objects.create(name=name,option=option,exp=exp)
        ex.save()
        return render(request,"index.html")
    else:
        x=experience.objects.all()
        data=list()
        for i in x:
            if(i.option=="depression"):
                data.append(
                {
                    'name':i.name,
                    'exp':i.exp,
                }
            ) 
        return render(request,"Deppression.html",{'data':data})
def anger(request):
    if(request.method=="POST"):
        name=request.POST['name']
        option=request.POST['option']
        exp=request.POST['feedback']
        ex=experience.objects.create(name=name,option=option,exp=exp)
        ex.save()
        return render(request,"index.html")
    else:
        x=experience.objects.all()
        data=list()
        for i in x:
            if(i.option=="anger"):
                data.append(
                {
                    'name':i.name,
                    'exp':i.exp,
                }
            ) 
        return render(request,"Anger.html",{'data':data})

def bullying(request):
    if(request.method=="POST"):
        name=request.POST['name']
        option=request.POST['option']
        exp=request.POST['feedback']
        ex=experience.objects.create(name=name,option=option,exp=exp)
        ex.save()
        return render(request,"index.html")
    else:
        x=experience.objects.all()
        data=list()
        for i in x:
            if(i.option=="bullying"):
                data.append(
                {
                    'name':i.name,
                    'exp':i.exp,
                }
            ) 
        return render(request,"Bullying.html",{'data':data})
    
def grief(request):
    if(request.method=="POST"):
        name=request.POST['name']
        option=request.POST['option']
        exp=request.POST['feedback']
        ex=experience.objects.create(name=name,option=option,exp=exp)
        ex.save()
        return render(request,"index.html")
    else:
        x=experience.objects.all()
        data=list()
        for i in x:
            if(i.option=="grief"):
                data.append(
                {
                    'name':i.name,
                    'exp':i.exp,
                }
            ) 
        return render(request,"Grief.html",{'data':data})
def anxiety(request):
    if(request.method=="POST"):
        name=request.POST['name']
        option=request.POST['option']
        exp=request.POST['feedback']
        ex=experience.objects.create(name=name,option=option,exp=exp)
        ex.save()
        return render(request,"index.html")
    else:
        x=experience.objects.all()
        data=list()
        for i in x:
            if(i.option=="anxiety"):
                data.append(
                {
                    'name':i.name,
                    'exp':i.exp,
                }
            ) 
        return render(request,"Anxiety.html",{'data':data})
def dashboard(request):
    x=User.objects.all()
    n=len(x)
    y=experience.objects.all()
    d=list()
    a=0
    dep=0
    an=0
    b=0
    g=0
    for i in y:
        if(i.option=="anxiety"):
            a=a+1
        elif(i.option=="depression"):
            dep=dep+1
        elif(i.option=="anger"):
            an=an+1
        elif(i.option=="bullying"):
            b=b+1
        else:
            g=g+1
    data={'Anxiety':a,'Depression':dep,'Anger':an,'Bullying':b,'Grief':g}

    return render(request,"dashboard.html",{'n':n,'data':data})
    
