from django.shortcuts import render
from django.http import HttpResponse
from userapp.form import userForm,logForm,productForm
from userapp.models import Company_User,Company_Product

# Create your views here.
def home(request):
    d=userForm()
    return render(request,'home.html',{"f":d})
def reg(request):
    try:
        if request.method=='POST':
            r1=userForm(request.POST)
            if r1.is_valid():
                r1.save() 
        return render(request,'home.html',{'f':r1,"msg":" Successfully Added "})
    except Exception as e:
        print(e)
        return HttpResponse("Error")

def logpage(request):
    d=logForm()
    return render(request,'login.html',{"f":d})

def logacc(request):
    message={}
    d=logForm()
    try:
        loginname=request.POST['name']
        loginpassword=request.POST['password']
        request.session['username']=loginname
        print(loginpassword)
        che=Company_User.objects.filter(name=loginname,password=loginpassword)
        if che.exists():
            return display(request)
        else:
            message['msg']="login failed"
            return render(request,"login.html",{"f":d},message)
    except Exception as e:
        print(e)
        message['msg6']="Failed"
        return render(request,"userpage.html",message)

def display(request):
    d=productForm()
    show=Company_Product.objects.all()
    return render(request,"userpage.html",{"f":d,"form":show})

def pro_add(request):
    d=productForm()
    try:
        if request.method=='POST':
            r1=productForm(request.POST)
            if r1.is_valid():
                r1.save() 
                show=Company_Product.objects.all()
        return render(request,'userpage.html',{'f':r1,"form":show,"msg":" Successfully Added "})
    except Exception as e:
        print(e)
        return HttpResponse("Error")

def productdel(request):
    if 'del' in request.POST:
        if request.method=='POST':
            d=productForm()
            show=Company_Product.objects.all()
            pid=request.POST['selectproduct']
            emp1=Company_Product.objects.filter(Product_id=pid)
            emp1.delete()
            return render(request,"userpage.html",{"form":d,"form":show})
    if 'get' in request.POST:
        if request.method=='POST':
            d=productForm()
            show=Company_Product.objects.all()
            pid=request.POST['selectproduct']
            emp1=Company_Product.objects.filter(Product_id=pid)
            return render(request,"userpage.html",{"form":d,"form":show,'form4':emp1})

def productup(request):
    if request.method=='POST':
        qu=request.POST['prate']
        pname=request.POST['prname']
        d=productForm()
        show=Company_Product.objects.all()
        emp1=Company_Product.objects.filter(Product_name=pname)
        emp1.update(Product_quantity=qu)
        return render(request,"userpage.html",{"form":d,"form":show,'msg2':"Details Updated"})
      