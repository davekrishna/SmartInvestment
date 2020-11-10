from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import blogPosts,Comments,Replys,Contact,Subscribed
from .forms import commentform,replyform,ContactForm
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method=='GET':
        blogsobj=blogPosts.objects.all()
    else:
        if request.POST.get('SubscribePOST'):
            subscribe(request.POST.get('emailId'))
            blogsobj=blogPosts.objects.all()
    return render(request,'home.html',{'blogsObj':blogsobj})


def Article(request,blogname):
    if request.method=="POST":
        print('inside post request')
        if request.POST.get('savecomment'):
            #post comment done
            commentToSave=commentform(request.POST)
            if commentToSave.is_valid():
                name=request.POST.get('commentByName')
                email=request.POST.get('commentByEmail')
                commentvar=request.POST.get('comment')
                blog_id=request.POST.get('blogid')
                blogobj=blogPosts.objects.get(id=blog_id)
                commentobj=Comments.objects.create(ForblogPost=blogobj,commentByName=name,commentByEmail=email,comment=commentvar)
                commentobj.save()
                print('comment saved')
            else:
                messages.info(request,'invalid values please try again')   
            
        elif request.POST.get('SubscribePOST'):
            subscribe(request.POST.get('emailId'))
            blog_id=request.POST.get('blogid')
            blogobj=blogPosts.objects.get(id=blog_id)

        elif request.POST.get('likecomment'):
            #post for comment like
            commentid=request.POST.get('id')
            commentobj=Comments.objects.get(id=commentid)
            commentobj.likes+=1
            commentobj.save()
            blog_id=request.POST.get('blogid')
            blogobj=blogPosts.objects.get(id=blog_id)

        elif request.POST.get('dislikecomment'):
            #post for comment dislike
            commentid=request.POST.get('id')
            commentobj=Comments.objects.get(id=commentid)
            commentobj.dislikes+=1
            commentobj.save()
            blog_id=request.POST.get('blogid')
            blogobj=blogPosts.objects.get(id=blog_id)

        elif request.POST.get('savereply'):
            #post reply done
            replyToSave=replyform(request.POST)
            if replyToSave.is_valid():
                name=request.POST.get('ReplyByName')
                email=request.POST.get('ReplyByEmail')
                commentid=request.POST.get('commentid')
                print('comment id',commentid)
                commentsobj=Comments.objects.get(id=commentid)
                blog_id=request.POST.get('blogid')
                print('blog id',blog_id)
                blogobj=blogPosts.objects.get(id=blog_id)
                replyvar=request.POST.get('reply')
                replyobj=Replys.objects.create(ForblogPost=blogobj,ForComment=commentsobj,ReplyByName=name,ReplyByEmail=email,reply=replyvar)
                replyobj.save()
            else:
                messages.info(request,'invalid values please try again')

        elif request.POST.get('likereply'):
            #post for reply like
            replyid=request.POST.get('id')
            replyobj=Replys.objects.get(id=replyid)
            replyobj.likes+=1
            replyobj.save()
            blog_id=request.POST.get('blogid')
            blogobj=blogPosts.objects.get(id=blog_id)

        elif request.POST.get('dislikereply'):
            #post for reply dislike
            replyid=request.POST.get('id')
            replyobj=Replys.objects.get(id=replyid)
            replyobj.dislikes+=1
            replyobj.save()
            blog_id=request.POST.get('blogid')
            blogobj=blogPosts.objects.get(id=blog_id)

        return redirect('blog_module:articlePg',blogname=blogobj.Title)
    else:
        blogsobj=blogPosts.objects.get(Title=blogname)
        commentformobj=commentform()
        replyformobj=replyform()
        commentsobj=Comments.objects.filter(ForblogPost=blogsobj).order_by('TimeOfComment')
        replysobj=Replys.objects.filter(ForblogPost=blogsobj)
        return render(request,'article.html',{'blogsObj':blogsobj,'comments':commentsobj,'CommentForm':commentformobj,'replys':replysobj,'ReplyForm':replyformobj})
        
    
def ArticleList(request):
    if request.method=='GET':
        blogsobj=blogPosts.objects.all()
        return render(request,'articlelistpg.html',{'blogsObj':blogsobj})
    else:
        if request.POST.get('SubscribePOST'):
            subscribe(request.POST.get('emailId'))
            return redirect('blog_module:articleListPg')
        blogid=request.POST.get('blogid')
        blogsobj=blogPosts.objects.get(id=blogid)
        return redirect('blog_module:articlePg',blogname=blogsobj.Title)


def ContactFunct(request):
    if request.method=='POST':
        if request.POST.get('SubscribePOST'):
            subscribe(request.POST.get('emailId'))
        elif request.POST.get('contactForm'):
            contactform=ContactForm(request.POST)
            if contactform.is_valid():
                contactform.save()
                print('form saved')
    formContact=ContactForm()
    return render(request,'contactpage.html',{'contactForm':formContact})

    

def subscribe(mailId):
    print('subscribe post received for email id',mailId)
    Subscriptionobj=Subscribed.objects.create(EmailId=mailId)
    Subscriptionobj.save()
    return 