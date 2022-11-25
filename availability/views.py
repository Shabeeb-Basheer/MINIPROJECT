from django.shortcuts import render
from availability.models import Availability
from booking.models import Booking
from register_user.models import RegisterUser
from packages.models import Packages
# Create your views here.
def a(request):
    if request.method=="POST":
        obj=Availability()
        obj.available_date=request.POST.get('a')
        obj.save()
    return render(request,'availability/post.html')





def v(request):
    obj=Availability.objects.all()
    context={
        'q':obj
    }
    return render(request,'availability/view.html',context)

def book(request,idd):
    obj1 = RegisterUser.objects.all()
    obj2 = Packages.objects.all()
    obj = Availability.objects.get(a_id=idd)
    context = {
        'q': obj,
        'p': obj2,
        'o': obj1
    }

    if request.method == "POST":
        ob = Booking()
        ob.service_id = request.POST.get('ser')
        ob.user_id = request.POST.get('user')
        ob.package_id = request.POST.get('s')
        ob.ac_status = request.POST.get('g')
        ob.time_status = request.POST.get('t')
        ob.date = request.POST.get('date')
        ob.status = 'ok'
        ob.save()


        obb=Availability.objects.get(a_id=idd)
        obb.status='Booked'
        obb.save()
        return v(request)
    return render(request, 'booking/booking.html', context)
