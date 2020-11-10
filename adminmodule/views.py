from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.models import User,auth
from django.contrib import messages
from blogPostModule.forms import BlogForm,BlogContent,editBlogcontent
from blogPostModule.models import blogPosts,Contact
from django.conf import settings
from django.core.mail import EmailMessage

# Create your views here.
def adminIndex(request):
    formLogin=forms.AdminLogin()
    formRegister=forms.AdminRegistration()
    return render(request,'index2.html',{'LoginForm':formLogin,'RegisterForm':formRegister})

def ARegister(request):
    if(request.method=='POST'):
        print('register request')
        formRegister=forms.AdminRegistration(request.POST)
        name=request.POST.get('Username')
        email=request.POST.get('Email')
        pwd=request.POST.get('Password')            
        cpwd=request.POST.get('confirmPassword')
        print(name,email,pwd,cpwd)
        if formRegister.is_valid():
            #print('validform')
            if(cpwd==pwd):
                if(User.objects.filter(username=name)).exists():
                    #username taken
                    messages.info(request,'username taken')
                    return redirect('admin_module:adminindex')
                elif(User.objects.filter(email=email).exists()):
                    #email used
                    messages.info(request,'email taken')
                    return redirect('admin_module:adminindex')
                else:
                    user=User.objects.create_superuser(username=name,password=pwd,email=email)
                    user.save()
                    messages.info(request,'registration successfull try login')
                    #user is  created
                    #either u use httpresponseredirect with url as parameter
                    return redirect('admin_module:adminindex')
            else:
                #print('pwd and cpwd doesnt match') 
                messages.info(request,'Confirm password must match password')
                #or u use appname:viewname(the third parameter name in url) in ur redirect argument
                return redirect('admin_module:adminindex')
        else:
                #print('invalid form')
                messages.info(request,'invalid form plz try again')
                return redirect('admin_module:adminindex')
            
    else:
        return render(request,'index2.html')

def ALogin(request):
    if(request.method=='POST'):
        print('login request')
        formLogin= forms.AdminLogin(request.POST)
        name=request.POST.get('Username')
        pwd=request.POST.get('Password')
        user=auth.authenticate(username=name,password=pwd)
        if formLogin.is_valid():
            if user is not None:
                if user.is_superuser:
                    auth.login(request,user)
                    request.session['username']=name
                    request.session['password']=pwd
                    return redirect('admin_module:adminHomepg')
                else:
                    messages.info(request,'invalid credentials')
                    return redirect('admin_module:adminindex')
            else:
                messages.info(request,'no such user.plz register first')
                return redirect('admin_module:adminindex')

def Admin(request):
    if request.user.is_authenticated:
        if(request.method=='GET'):
            formblog=BlogForm()
            editForm=editBlogcontent()
            print('admin authenticated')
            return render(request,'adminhome.html',{'formBlog':formblog,'formBlogEdit':editForm})
        else:
            if request.POST.get('addBlog'):
                formblog=BlogForm(request.POST,request.FILES)
                blogname=request.POST.get('Title')
                print('title',blogname)
                if formblog.is_valid():
                    formblog.save()
                    modelBlogobj=blogPosts.objects.get(Title=blogname)
                    request.session['blogid']=modelBlogobj.id
                    return redirect('admin_module:addPostPage')
                else:
                    print('invalid form')
                    messages.info(request,'plz try again')
                    return redirect('admin_module:adminHomepg')
            elif request.POST.get('editBlog'):
                editForm=editBlogcontent(request.POST)
                blogname=request.POST.get('Title')
                if editForm.is_valid():
                    modelBlogobj=blogPosts.objects.get(Title=blogname)
                    if(modelBlogobj):
                        request.session['blogid']=modelBlogobj.id
                        return redirect('admin_module:editPostPage')
                    else:
                        messages.info(request,'no such blog exists')
                        return redirect('admin_module:adminHomepg')
                else:
                    print('invalid form')
                    messages.info(request,'plz try again')
                    return redirect('admin_module:adminHomepg')
    else:
        return redirect('admin_module:adminindex')


def addPostFunct(request):
    if(request.method=='GET'):
        ContentForm=BlogContent()
        return render(request,'addContents.html',{'formContent':ContentForm})
    else:
        ContentForm=BlogContent(request.POST)
        if ContentForm.is_valid():
            blogid=request.session['blogid']
            modelblogobj=blogPosts.objects.get(id=blogid)
            modelblogobj.Content=request.POST.get('Content')
            modelblogobj.save()
            print('contents saved')
            messages.info(request,'blog connents saved')
        return redirect('admin_module:adminHomepg')
        
def editPostFunct(request):
    blogid=request.session['blogid']
    modelBlogobj=blogPosts.objects.get(id=blogid)
    if(request.method=='GET'):
        blogForm1=BlogForm(initial={'Title':modelBlogobj.Title})
        return render(request,'editPost.html',{'form1':blogForm1})
    else:
        if request.POST.get('editIntro'):
            blogForm1=BlogForm(request.POST,request.FILES)
            modelBlogobj.Title= request.POST.get('Title')
            if(modelBlogobj.thumbnail):
                modelBlogobj.thumbnail.delete(False)
            modelBlogobj.thumbnail=request.FILES.get('thumbnail')
            modelBlogobj.save()
            messages.info(request,'intro details edited succcessfully')
            return redirect('admin_module:editPostPage')
        elif request.POST.get('editContents'):
            blogForm2=BlogContent(initial={'Content':modelBlogobj.Content})
            return render(request,'editContents.html',{'form':blogForm2})
        return redirect('admin_module:adminHomepg')


def ReplyContacted(request):
    if request.method=='GET':
        obj=Contact.objects.filter(isReplied="False")
        formMailReply=forms.ContactReplyForm()
        return render(request,'ReplyContacted.html',{'ContactList':obj,'MailReply':formMailReply})
    else:
        contactid=request.POST.get('Contactid')
        print(contactid)
        mailcontents=forms.ContactReplyForm(request.POST)
        print(mailcontents)
        print('contact id',contactid)
        contactobj=Contact.objects.get(id=contactid)
        mailFrom=settings.EMAIL_HOST_USER
        MailTo=[contactobj.Uemail,]
        Subject=mailcontents['Subject'].value()
        print('subject',Subject)
        message=mailcontents['Msg'].value()
        print('message',message)
        Mail=EmailMessage(Subject,message,mailFrom,MailTo)
        Mail.send()
        contactobj.isReplied=True
        contactobj.save()
        return redirect('admin_module:replyCommentsPg')
