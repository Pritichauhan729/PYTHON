from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from chairmanapp.models import *

# Create your views here.

# def home(request):
#     if "email" in request.session:
#         uid = User.objects.get(email = request.session['email'])
#         sid = Societymember.objects.get(user_id = uid)
#         context = {
#             'uid' : uid,
#             'sid' : sid,
#         }
#         return render(request,"societymemberapp/index.html",context)
#     else:    
#          return redirect("login")
def societymember_profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role=="societymember":
            sid = Societymember.objects.get(user_id = uid)
            context = {
                'uid' : uid,
                'sid' : sid,
            }
            return render(request,"societymemberapp/profile.html",context)
    else:
        return redirect("login") 

def societymember_change_password(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        sid = Societymember.objects.get(user_id = uid)

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
                'sid' : sid,
            }
            return render(request,"societymemberapp/profile.html",context)
    else:
        context = {
            'uid' : uid,
            'sid' : sid,
        }
        return render(request,"societymemberapp/profile.html",context)

def view_notice_society(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        sid = Societymember.objects.get(user_id = uid)
        nall = Notice.objects.all()
        context = {
            'uid' : uid,
            'sid' : sid,
            'nall' : nall,

        }
        return render(request,"societymemberapp/notice-list.html",context)
        
 
def view_notice_society_details(request,pk):
    if "email" in request.session:
        print("------------>PK",pk)
        uid = User.objects.get(email = request.session['email'])
        sid = Societymember.objects.get(user_id = uid)
        notice_id = Notice.objects.get(id = pk)

        

        nall = NoticeViewDetails.objects.filter(user_id = uid,notice_id = notice_id)
        
        if len(nall) == 0:
           nid = NoticeViewDetails.objects.create(user_id = uid,notice_id = notice_id)
         
        

        

        notice = Notice.objects.filter(id = pk)
        context = {
            'uid' : uid,
            'sid' : sid,
            'notice' :notice,

        }
        return render(request,"societymemberapp/notice-details.html",context)

        

                                                                                                 