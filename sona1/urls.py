from django.contrib import admin
from django.urls import path
from enroll import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('index/',views.getfile,name='index'),
    path('mail/',views.mail,name='mail')
]
