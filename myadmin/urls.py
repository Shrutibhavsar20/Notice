"""
URL configuration for notice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myadmin import views


urlpatterns = [
    path('admin/', admin.site.urls),
	path('layout', views.layout, name='layout'),
	path('dashboard', views.dashboard, name='dashboard'),

   path('add_state', views.add_state, name='add_state'),
   path('state_store', views.state_store, name='state_store'),
   path('all_state', views.all_state, name='all_state'),
   path('delete_state/<int:id>', views.delete_state, name='delete_state'),
   path('edit_state/<int:id>', views.edit_state, name='edit_state'),
   path('update_state/<int:id>', views.update_state, name='update_state'),

   path('add_city', views.add_city, name='add_city'),
   path('store_city', views.store_city, name='store_city'),
   path('all_city', views.all_city, name='all_city'),
   path('delete_city/<int:id>', views.delete_city, name='delete_city'),
    path('edit_city/<int:id>', views.edit_city, name='edit_city'),
   path('update_city/<int:id>', views.update_city, name='update_city'),

   path('add_area', views.add_area, name='add_area'),
   path('store_area', views.store_area, name='store_area'),  
   path('all_area', views.all_area, name='all_area'),
   path('delete_area/<int:id>', views.delete_area, name='delete_area'),
   path('edit_area/<int:id>', views.edit_area, name='edit_area'),
   path('update_area/<int:id>', views.update_area, name='update_area'),

   path('users', views.users, name='users'),
   path('detail_customer/<int:id>', views.detail_customer, name='detail_customer'),

   path('verify/<int:id>', views.verify, name='verify'),

   path('add_notice', views.add_notice, name='add_notice'),
   path('notice_store', views.notice_store, name='notice_store'),
   path('all_notice', views.all_notice, name='all_notice'),
   path('notice_delete/<int:id>', views.notice_delete, name='notice_delete'),
   path('notice_edit/<int:id>', views.notice_edit, name='notice_edit'),
   path('notice_update/<int:id>', views.notice_update, name='notice_update'),

   path('login', views.login, name='login'),
   path('login_check', views.login_check, name='login_check'),
   path('logout', views.logout, name='logout'),

   path('inquiry', views.inquiry, name='inquiry'),




















]

