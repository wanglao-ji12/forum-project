from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    headportrait=models.ImageField()
    signature=models.CharField(max_length=50)
    pass

class Comment(models.Model):
    c_User_id=models.OneToOneField(User,on_delete=models.DO_NOTHING)
    c_Content=models.CharField(max_length=500)
    c_Date=models.DateField()
    c_Likes=models.IntegerField(default=0)


class Posting(models.Model):
    landlord_id=models.OneToOneField(User,on_delete=models.DO_NOTHING)
    p_Title=models.CharField(max_length=20)
    p_Describtion=models.CharField(max_length=200)
    p_Date=models.DateField()
    p_Comments_id=models.ForeignKey(Comment,on_delete=models.CASCADE)

class Collection(models.Model):
    User_id=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    Posting_id=models.ForeignKey(Posting,on_delete=models.DO_NOTHING)


