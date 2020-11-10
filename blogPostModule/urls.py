from django.urls import path
from . import views
app_name='blog_module'
urlpatterns=[
    path('',views.home,name='homepg'),
    path('articleList',views.ArticleList,name='articleListPg'),
    path('article/<str:blogname>',views.Article,name='articlePg'),
    path('contact',views.ContactFunct,name='contactPg'),
]