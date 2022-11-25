from django.shortcuts import render
from packages.models import Packages
# Create your views here.
def post(request):
    if request.method=="POST":
        ob=Packages()
        ob.package_name=request.POST.get('pname')
        ob.description=request.POST.get('des')
        ob.status="pending"
        ob.save()
    return render(request,'packages/packagemanage.html')

def view(request):
    obj=Packages.objects.all()
    context={
        'x':obj
    }
    return render(request,'packages/packageview.html',context)

def appr(request,idd):
    obj=Packages.objects.get(package_id=idd)
    obj.status="approved"
    obj.save()
    return view(request)

def rej(request,idd):
    obj=Packages.objects.get(package_id=idd)
    obj.status="rejected"
    obj.save()
    return view(request)




def user(request):
    obj=Packages.objects.filter(status='approved')
    context={
        'o':obj
    }
    return render(request,'packages/packageviewadmin.html',context)
