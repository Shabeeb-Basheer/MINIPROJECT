from django.shortcuts import render
from booking.models import Booking
from quotation.models import Quotation
from services.models import Services
from facilities.models import Facilities
from packages.models import Packages
from register_user.models import RegisterUser
# Create your views here.
def post_book(request):
    obj1=RegisterUser.objects.all()
    obj=Packages.objects.all()
    # obb=Services.objects.all()
    context={
        'p':obj,
        # 'u':obb,
        'o':obj1
    }
    if request.method=="POST":
        ob=Booking()
        ob.service_id=request.POST.get('ser')
        ob.user_id=request.POST.get('user')
        ob.package_id=request.POST.get('s')
        ob.ac_status=request.POST.get('g')
        ob.time_status=request.POST.get('t')
        ob.date=request.POST.get('date')
        ob.no_of_people=request.POST.get('number')
        ob.status='ok'
        ob.save()
    return render(request,'booking/booking.html',context)

def view(request):
    obj=Booking.objects.all()
    context={
        'x':obj
    }
    return render(request,'booking/bookingview.html',context)


def user(request):
    ss=request.session["uid"]
    obj=Booking.objects.filter(status='ok',user_id=ss)
    context={
        'l':obj
    }
    return render(request,'booking/mangeuser.html',context)





def can(request,idd):
    obj=Booking.objects.get(booking_id=idd)
    obj.status="cancelled"
    obj.save()
    return user(request)





def aprve(request,idd):
    obj=Booking.objects.get(booking_id=idd)
    obj.owner_status="approved"
    obj.save()
    return view(request)






def rejct(request,idd):
    obj=Booking.objects.get(booking_id=idd)
    obj.owner_status="Rejected"
    obj.save()
    return view(request)



def quation(request,idd):
    ob=Booking.objects.get(booking_id=idd)
    context={
        'x':ob
    }
    if request.method=="POST":
        obj=Quotation()
        obj.quotation_name=request.POST.get('qname')
        obj.description=request.POST.get('des')
        obj.status='pending'
        obj.user_id=ob.user_id
        obj.save()
        return view(request)
    return render(request, 'quotation/qoutationpost.html',context)
