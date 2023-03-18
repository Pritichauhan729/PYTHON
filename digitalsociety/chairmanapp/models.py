from django.db import models
from django.utils import timezone
import math

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True,max_length=30,blank=False)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    is_verify = models.BooleanField(default=False)
    otp = models.IntegerField(default=456)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Chairman(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=30)
    pic = models.FileField(upload_to="media/upload", default="media/default.png")

    def __str__(self):
        return self.firstname


class Societymember(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=30)
    block_no = models.CharField(max_length=10)

    def __str__(self):
        return self.firstname

class Notice(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def count_view(self):
        ncount = NoticeViewDetails.objects.filter(notice_id = self._id).count()
        print("========>> ncount ",ncount)
        return ncount

    


class NoticeViewDetails(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    notice_id = models.ForeignKey(Notice,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Event(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def count_view(self):
        ncount = NoticeViewDetails.objects.filter(notice_id = self._id).count()
        print("========>> ncount ",ncount)
        return ncount

    


class EventViewDetails(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    notice_id = models.ForeignKey(Event,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
   