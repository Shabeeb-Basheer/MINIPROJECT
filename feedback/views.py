from django.shortcuts import render
from feedback.models import Feedback
# Create your views here.


def post(request):
    if request.method=="POST":
        ob=Feedback()
        ob.feedback=request.POST.get('feedback')
        ob.user_id=1
        ob.save()
    return render(request,'feedback/feedback.html')

def view(request):
    obj=Feedback.objects.all()
    context={
        'x':obj
    }
    return render(request,'feedback/feedbackview.html',context)