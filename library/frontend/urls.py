from django.urls import path,include
from .views import publicView,privateAllView,filedownloadView,loginForm,logoutFunc,downloadSearchView
urlpatterns =[
    path("",publicView,name="main_view"),
    path("private/",privateAllView,name="private"),
    path("auth/login/",loginForm,name="login_form"),
    path("item/download/<str:i>",filedownloadView,name="download_view"),
    path("auth/logout/",logoutFunc,name="logout"),
    path("item/download",downloadSearchView,name="download_form_view")
 ]