from django.shortcuts import render
from register_user.models import RegisterUser
from login.models import Login
# Create your views here.
def post(request):
    if request.method=="POST":
        ob=RegisterUser()
        ob.name=request.POST.get('name')
        ob.age=request.POST.get('age')
        ob.address=request.POST.get('addr')
        ob.gender=request.POST.get('gender')
        ob.place=request.POST.get('place')
        ob.mobile_number=request.POST.get('number')
        ob.email=request.POST.get('mail')
        ob.password=request.POST.get('password')
        ob.save()


        obj=Login()
        obj.username=ob.name
        obj.password=ob.password
        obj.u_id=ob.user_id
        obj.type='user'
        obj.save()

    return render(request,'register_user/register.html')