from django.shortcuts import render
from facilities.models import Facilities
# Create your views here.
def post(request):
    if request.method=="POST":
        ob=Facilities()
        ob.facility_name=request.POST.get('fname')
        ob.description=request.POST.get('des')
        ob.status="pending"
        ob.save()
    return render(request,'facilities/facilitymanage.html')

def view(request):
    obj=Facilities.objects.all()
    context={
        'x':obj
    }
    return render(request,'facilities/facilityview.html',context)

def approv(request,idd):
    obj=Facilities.objects.get(facility_id=idd)
    obj.status="approved"
    obj.save()
    return view(request)

def rejec(request,idd):
    obj=Facilities.objects.get(facility_id=idd)
    obj.status="rejected"
    obj.save()
    return view(request)



def user(request):
    obj=Facilities.objects.filter(status='approved')
    context={
        'p':obj
    }
    return render(request,'facilities/facilityviewuser.html',context)
