from django import forms  
from django.core.exceptions import ValidationError
from .models import blogPosts,Comments,Replys,Contact
import re

class BlogForm(forms.ModelForm):
    class Meta:
        model=blogPosts
        fields=["Title","thumbnail"]
        labels={
            "Title":'enter blog title',
            "thumbnail":"select thumbnail image",
        }
        widgets={
            "Title":forms.TextInput(attrs={'class':'form-control-file','id':'title','name':'title'}),
            "thumbnail":forms.FileInput(attrs={'class':'form-control-file','id':'thumbnail','name':'thumbnail'}),      
        }

class BlogContent(forms.ModelForm):
    class Meta:
        model=blogPosts
        fields=["Content"]
        labels={
            "Content":"Contents"
        }
        widgets={
            "Content":forms.TextInput(attrs={'class':'form-control-file','id':'contents'}),
        }

class editBlogcontent(forms.ModelForm):
    class Meta:
        model=blogPosts
        fields=['Title']
        labels={
            "Title":'enter blog title',
        }
        widgets={
            "Title":forms.TextInput(attrs={'class':'form-control-file','id':'title','name':'title'}),
        }

class commentform(forms.ModelForm):
    class Meta:
        model=Comments
        fields=["commentByName","commentByEmail","comment"]
        labels={
            "commentByName":"Name",
            "commentByEmail":"Email",
            "comment":"Comment",
        }
        widgets={
            "commentByName":forms.TextInput(attrs={'class':'form-control align-self-center col-sm-4','placeholder':'Your name','id':'c_name'}),
            "commentByEmail":forms.TextInput(attrs={'class':'form-control align-self-center col-sm-4','placeholder':'Your email','id':'c_email'}),
            "comment":forms.Textarea(attrs={'class':'form-control align-self-center col-sm-4','placeholder':'Your message','id':'c_comment','rows':'3'}),
        }

    def validate_commentByName(self):
        value=self.cleaned_data['commentByName']
        if not re.compile('^[a-zA-Z]+$').match(value):
            print('error')
            raise ValidationError('Name can only contain letters')
        else:
            print('validation of name successed')

class replyform(forms.ModelForm):
    class Meta:
        model=Replys
        fields=['ReplyByName','ReplyByEmail','reply']
        labels={
            'ReplyByName':'Name',
            'ReplyByEmail':'Email',
            'reply':'Reply',
        }
        widgets={
            'ReplyByName':forms.TextInput(attrs={'class':'form-control input-sm','id':'r_name'}),
            'ReplyByEmail':forms.TextInput(attrs={'class':'form-control input-sm','id':'r_email'}),
            'reply':forms.Textarea(attrs={'class':'form-control input-sm','id':'r_reply','rows':'4'}),
        }

    def validate_ReplyByName(self):
        value=self.cleaned_data['ReplyByName']
        if not re.compile('^[a-zA-Z]+$').match(value):
            print('error')
            raise ValidationError('Name can only contain letters')
        else:
            print('validation of name successed')

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['firstName','lastName','Uemail','Reason']
        labels={
            'firstName':'First Name:',
            'lastName':'Last Name:',
            'Uemail':'Email:',
            'Reason':'Details:',
        }
        widgets={
            'firstName':forms.TextInput(attrs={'class':'form-control','placeholder':'your first name','id':'fname'}),
            'lastName':forms.TextInput(attrs={'class':'form-control','placeholder':'your last name','id':'lname'}),
            'Uemail':forms.TextInput(attrs={'class':'form-control','placeholder':'your email address','id':'emailid'}),
            'Reason':forms.Textarea(attrs={'class':'form-control','placeholder':'please describe the reason you want to contact us....','rows':'4','cols':'50','id':'reason'}),
        }

    def validate_firstName(self):
        value=self.cleaned_data['firstName']
        if not re.compile('^[a-zA-Z]+$').match(value):
            print('error')
            raise ValidationError('Name can only contain letters')
        else:
            print('validation of name successed')

    def validate_lastName(self):
        value=self.cleaned_data['lastName']
        if not re.compile('^[a-zA-Z]+$').match(value):
            print('error')
            raise ValidationError('Name can only contain letters')
        else:
            print('validation of name successed')


        