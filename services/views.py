from django.shortcuts import render
from services.models import Services
# Create your views here.
def post(request):
    if request.method=="POST":
        ob=Services()
        ob.service_name=request.POST.get('sname')
        ob.description=request.POST.get('des')
        ob.status="pending"
        ob.save()
    return render(request,'services/servicemanage.html')

def view(request):
    obj=Services.objects.all()
    context={
        'x':obj
    }
    return render(request,'services/serviceview.html',context)

def approve(request,idd):
    obj=Services.objects.get(service_id=idd)
    obj.status="approved"
    obj.save()
    return view(request)

def reject(request,idd):
    obj=Services.objects.get(service_id=idd)
    obj.status="Rejected"
    obj.save()
    return view(request)




def user(request):
    obj=Services.objects.filter(status='approved')
    context={
        'k':obj
    }
    return render(request,'services/serviceviewuser.html',context)
