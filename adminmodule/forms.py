from django import forms  
from django.core.exceptions import ValidationError
import re

class AdminRegistration(forms.Form):  
    
    def namevalidate(value):
        if not re.compile('^[a-zA-Z]+$').match(value):
            raise ValidationError('Name can only contain letters')
        else:
            print('validation of name successed')

    def pwdvalidate(value):
        if not re.compile('^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])([A-Za-z0-9@#$%^&+=_]+)').match(value):
            raise ValidationError('password wrong')
        else:
            print('validation of password successed')

    Username = forms.CharField(
        label="Enter user name",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'your name','id':'name'}),
        validators=[namevalidate],
        )
    Email = forms.EmailField(
        label="Enter your email", 
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'your email id','id':'emailid'}),
        )  
    Password=forms.CharField(
        label="Enter Password",
        min_length=8,
        max_length=50,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'your password','id':'pwd'}),
        validators=[pwdvalidate],
        )
    confirmPassword=forms.CharField(
        label="confirm Password",
        min_length=8,
        max_length=50,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'confirm password','id':'cpwd'}),
        )


class AdminLogin(forms.Form):
    def namevalidate(value):
        if not re.compile('^[a-zA-Z]+$').match(value):
            raise ValidationError('Name can only contain letters')
        else:
            print('validation of name successed')

    def pwdvalidate(value):
        if not re.compile('^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])([A-Za-z0-9@#$%^&+=_]+)').match(value):
            raise ValidationError('password wrong')
        else:
            print('validation of password successed')

    Username = forms.CharField(
        label="Enter user name",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'your name','id':'name'}),
        validators=[namevalidate],
        )
    Password=forms.CharField(
   
        label="Enter Password",
        min_length=8,
        max_length=50,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'your password','id':'pwd'}),
        validators=[pwdvalidate],
        )

class ContactReplyForm(forms.Form):
    Subject=forms.CharField(
        label='Enter Subject',
        widget=forms.TextInput(attrs={'class':'form-control','id':'sub'}),
    )
    Msg=forms.CharField(
        label='Enter message',
        widget=forms.Textarea(attrs={'class':'form-control','id':'msg'}),
    )