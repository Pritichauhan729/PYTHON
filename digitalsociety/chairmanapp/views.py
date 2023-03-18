from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *
from random import *
from django.core.mail import send_mail

# Create your views here.

"""
get() : return object

models.object.get(fieldname = html)  : fetch data from database (model).



uid model.object.get()
uid.fieldname = newvalue
uid.save()  : for update data

# store data in model  (similar like insert query)
uid = model.object.create(fieldname=pythonname,fieldname=pythoname) 


# fetch all data from model (without any condition)

var = model.object.all()

e.g. Notice.object.all()

# fetch all data from model but condition wise

filter() : queryset

var = models.object.filter(fieldname = value )


"""

def home(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role=="chairman":
            cid = Chairman.objects.get(user_id = uid)
            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render(request,"chairmanapp/index.html",context)
        else:
            if uid.role=="societymember":
                sid = Societymember.objects.get(user_id = uid)
                context = {
                    'uid' : uid,
                    'sid' : sid,
                }
                return render(request,"societymemberapp/index.html",context)

    else:    
         return redirect("login")
    

def login(request):
    if "email" in request.session:
        return redirect('home')
    else:    
        if request.POST:
            pemail = request.POST['email']
            ppassword = request.POST['password']
            print("--------->email ",pemail)
            try:
                uid = User.objects.get(email = pemail)
                if uid.password ==ppassword:
                    if uid.role == "chairman":
                        cid = Chairman.objects.get(user_id = uid)

                        print("firstname ",cid.firstname)
                        print("SIGN IN BUTTON PRESS ---->" ,uid)
                        print(uid.role)
                        print(uid.password)
                        request.session['email'] = uid.email  # session store
                        return redirect("home")
                    else:
                        print("SOCIETY MEMBER") 
                        if uid.role == "societymember":
                            sid = Societymember.objects.get(user_id = uid)

                            print("firstname ",sid.firstname)
                            print("SIGN IN BUTTON PRESS ---->" ,uid)
                            print(uid.role)
                            print(uid.password)
                            request.session['email'] = uid.email  # session store
                            return redirect("home")   
                else:
                    context = {
                        'emsg' : "invalid password"
                    }
                    print("--->somthing went wrong")
                    return render(request,"chairmanapp/login.html",context)
            except:
                context = {
                    'emsg' : "invalid email address"
                }
                print("====>something went wrong")
                return render(request,"chairmanapp/login.html",context)
        else:
            print("===> login page refresh")
            return render(request,"chairmanapp/login.html")                    
        
def logout(request):
    if "email" in request.session:
        del request.session['email']
        return redirect("login")
    else:
        return redirect("login")

def chairman_profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        if request.POST:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']

            cid.firstname = firstname
            cid.lastname = lastname
            if "picture" in request.FILES:
                cid.pic = request.FILES['picture']

            cid.save()
            
            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render(request,"chairmanapp/profile.html",context)
        else:
            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render(request,"chairmanapp/profile.html",context)
    else:
        return redirect("login") 

def chairman_change_password(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)

        if request.POST:
            currentpassword = request.POST['Currentpassword']
            newpassword = request.POST['newpassword']

            if uid.password == currentpassword :
                uid.password = newpassword
                uid.save()
                return redirect("logout")
            else:
                pass    

            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render(request,"chairmanapp/profile.html",context)
    else:
        context = {
            'uid' : uid,
            'cid' : cid,
        }
        return render(request,"chairmanapp/profile.html",context)

def add_member(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        context = {
            'uid' : uid,
            'cid' : cid,
        }
        return render(request,"chairmanapp/add-member.html",context)
    else:
        return redirect("login") 

def add_notice(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)

        if request.POST:
            nid = Notice.objects.create(
                user_id = uid,
                title = request.POST['title'],
                description = request.POST['description'],
            )

            nall = Notice.objects.all()
            context = {
                'uid' : uid,
                'cid' : cid,
                'nall' : nall,
            }
            
            return render(request,"chairmanapp/notice-list.html",context)

        else:
            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render(request,"chairmanapp/add-notice.html",context)
    else:
        return redirect("login")

     
def view_notice(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        nall = Notice.objects.all()
        


        context = {
            'uid' : uid,
            'cid' : cid,
            'nall' : nall,

        }
        return render(request,"chairmanapp/notice-list.html",context)
        
 
def view_notice_details(request,pk):
    if "email" in request.session:
        print("------------>PK",pk)
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        notice = Notice.objects.filter(id = pk)
        context = {
            'uid' : uid,
            'cid' : cid,
            'notice' :notice,

        }
        return render(request,"chairmanapp/notice-details.html",context)

        
def forgot_password(request):
    if request.POST:
        email = request.POST['email']
        otp = randint(1111,9999)
        try:
            uid = User.objects.get(email = email)
            uid.otp = otp
            uid.save()
            send_mail("forgot password","your otp is"+str(otp),"warg0243@gmail.com",[email])
            context={
                'email' : email
            }
            return render(request,"chairmanapp/change-password.html",context)
        except:
            context = {
                "emsg" : "Invaild email address"
            }
            return render(request,"chairmanapp/forgot-password.html",context)
    return render(request,"chairmanapp/forgot-password.html")

def add_event(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)

        if request.POST:
            eid = Event.objects.create(
                user_id = uid,
                title = request.POST['title'],
                description = request.POST['description'],
            )

            eall = Event.objects.all()
            context = {
                'uid' : uid,
                'cid' : cid,
                'eall' : eall,
            }
            
            return render(request,"chairmanapp/event-list.html",context)

        else:
            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render(request,"chairmanapp/add-event.html",context)
    else:
        return redirect("login")

     
def view_event(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        eall = Event.objects.all()
        


        context = {
            'uid' : uid,
            'cid' : cid,
            'eall' : eall,

        }
        return render(request,"chairmanapp/event-list.html",context)
        
 
def view_event_details(request,pk):
    if "email" in request.session:
        print("------------>PK",pk)
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        event = Event.objects.filter(id = pk)
        context = {
            'uid' : uid,
            'cid' : cid,
            'event' : event,

        }
        return render(request,"chairmanapp/event-details.html",context)


                                                  