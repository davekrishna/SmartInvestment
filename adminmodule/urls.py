from django.urls import path
from . import views
app_name='admin_module'
urlpatterns=[
    path('EnterAsAdmin',views.adminIndex,name='adminindex'),
    path('AdminLogin',views.ALogin,name='login'),
    path('AdminRegister',views.ARegister,name='register'),
    path('admin',views.Admin,name='adminHomepg'),
    path('addPost',views.addPostFunct,name='addPostPage'),
    path('editPost',views.editPostFunct,name='editPostPage'),
    path('replyContacted',views.ReplyContacted,name='replyCommentsPg'),
]