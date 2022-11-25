from django.shortcuts import render
from login.models import Login
from django.http import HttpResponseRedirect
# Create your views here.
def post(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        obj = Login.objects.filter(username=name, password=password)
        tp =""
        for ob in obj:
            tp = ob.type
            uid = ob.u_id
            if tp == "admin":
                request.session["uid"] = uid
                return HttpResponseRedirect('/temp/adm/')
            elif tp == "user":
                request.session["uid"] = uid
                return HttpResponseRedirect('/temp/usr/')
            # elif tp == "customer":
            #     request.session["uid"] = uid
            #     return HttpResponseRedirect('/temp/tempcus/')
            #  elif tp == " ":
            #       request.session["uid"] = uid
            #      return render(request, 'temp/tempshop ')
        else:
            objilist = "username or password incorrect.....please try again.....!"
            context = {
                'msg': objilist,
                }
            return render(request, 'login/login.html', context)
    return render(request,'login/login.html')