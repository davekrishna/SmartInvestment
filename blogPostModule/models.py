from django.db import models

# Create your models here.

class blogPosts(models.Model):
    Title=models.CharField(max_length=500)
    thumbnail=models.FileField(upload_to='BlogPost/',null=True)
    Content=models.TextField()
    publishdate= models.DateTimeField(auto_now_add=True)
    likes=models.IntegerField(default=0)
    dislikes=models.IntegerField(default=0)


class Comments(models.Model):
    ForblogPost=models.ForeignKey(blogPosts,on_delete=models.CASCADE)
    commentByName=models.CharField(max_length=20)
    commentByEmail=models.EmailField()
    comment=models.TextField(max_length=150)
    TimeOfComment=models.DateTimeField(auto_now_add=True)
    likes=models.IntegerField(default=0)
    dislikes=models.IntegerField(default=0)

class Replys(models.Model):
    ForblogPost=models.ForeignKey(blogPosts,on_delete=models.CASCADE)
    ForComment=models.ForeignKey(Comments,on_delete=models.CASCADE)
    ReplyByName=models.CharField(max_length=20)
    ReplyByEmail=models.EmailField()
    reply=models.TextField(max_length=150)
    TimeOfReply=models.DateTimeField(auto_now_add=True)
    likes=models.IntegerField(default=0)
    dislikes=models.IntegerField(default=0)

class Contact(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    Uemail=models.EmailField()
    Reason=models.TextField(max_length=150)
    isReplied=models.BooleanField(default=False)

class Subscribed(models.Model):
    EmailId=models.EmailField()


