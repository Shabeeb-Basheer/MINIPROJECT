from django.shortcuts import render
from quotation.models import Quotation
from register_user.models import RegisterUser
# Create your views here.

def post(request):
    if request.method=="POST":
        ob=Quotation()
        ob.quotation_name=request.POST.get('qname')
        ob.description=request.POST.get('des')
        ob.status='pending'
        ob.save()
    return render(request,'quotation/qoutationpost.html')

def view(request):
    ss=request.session["uid"]
    obj=Quotation.objects.filter(user_id=ss,status='pending')
    context={
        'x':obj
    }
    return render(request,'quotation/qoutationview.html',context)

def app(request,idd):
    obj=Quotation.objects.get(quotation_id=idd)
    obj.status="approved"
    obj.save()
    return view(request)

def re(request,idd):
    obj=Quotation.objects.get(quotation_id=idd)
    obj.status="rejected"
    obj.save()
    return view(request)


def mm(request):
    obj=Quotation.objects.all()
    context={
        'y':obj
    }
    return render(request,'quotation/adview.html',context)
