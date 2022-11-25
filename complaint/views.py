from django.shortcuts import render
from complaint.models import Complaint
from register_user.models import RegisterUser
# Create your views here.
def post_comp(request):
    ob = RegisterUser.objects.all()
    context = {
        'w': ob
    }
    if request.method=="POST":
        ob=Complaint()
        ob.complaint=request.POST.get('cname')
        ob.user_id=request.POST.get('ur')
        ob.save()
    return render(request,'complaint/complaintpost.html',context)

def view(request):
    obj=Complaint.objects.all()
    context={
        'x':obj
    }
    return render(request,'complaint/complaintview.html',context)

def b(request,idd):
    ob=Complaint.objects.filter(complaint_id=idd)
    context={
        'x':ob
    }
    if request.method=="POST":
        obj=Complaint.objects.get(complaint_id=idd)
        obj.reply=request.POST.get('r')
        # obj.user_id=ss
        # obj.description=request.POST.get('des')
        obj.save()
        return view(request)
    return render(request, 'complaint/reply.html',context)


def reply(request):
    ss=request.session["uid"]
    obj=Complaint.objects.filter(user_id=ss)
    context={
        'u':obj
    }
    return render(request,'complaint/replyview.html',context)
