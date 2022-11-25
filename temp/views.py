from django.shortcuts import render

# Create your views here.
def admin(request):
    return render(request,'temp/admin.html')

def user(request):
    return render(request,'temp/user.html')

def form(request):
    return render(request,'temp/form.html')