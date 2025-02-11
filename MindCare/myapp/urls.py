from django.urls import path
from . import views
from .views import professionals_list
from .views import index, appointment_success
from .views import book_appointment
from django.shortcuts import render
from .views import get_available_slots
from django.urls import path
from .views import chat_room, get_messages, send_message
from .views import training_materials, upload_video
from .views import professional_detail
from .views import professional_dashboard

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout, name='logout'),
    path('post/<str:pk>', views.post, name='post'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('training_materials', views.training_materials, name='training_materials'),
    path('home', views.home, name='home.html'),
    path('room', views.room, name='room.html'),
    path('all', views.all, name='all.html'),
    path('mentorship/', views.mentorship_application, name='mentorship_application'),
    path('upload_video/', views.upload_video, name='upload_video'),
    path('send-info/', views.send_info, name='send_info'),
    path('contact', views.contact, name='contact'),
    path('professionals/create/', views.create_professional, name='create_professional'),
    #path('professionals/<int:pk>/', views.professional_detail, name='professional_detail'),
    path('professionals/', professionals_list, name='professionals_list'),
    path('appointment-success/', appointment_success, name='appointment_success'),
    path("book-appointment/", book_appointment, name="book_appointment"),
    path("appointment-success/", lambda request: render(request, "appointment_success.html"), name="appointment_success"),
    path('api/get-available-slots/<int:professional_id>/<str:date>/', get_available_slots, name='get_available_slots'),
    path("chat/<str:room_name>/", chat_room, name="chat_room"),
    path("anonymous_chat/", views.anonymous_chat, name="anonymous_chat"),
    path("get-messages/", views.get_messages, name="get_messages"),
    path("send-message/", views.send_message, name="send_message"),
    path("training_materials/", training_materials, name="training_materials"),
    path("upload_video/", upload_video, name="upload_video"),  # Admin-only upload page
    path("professionals/<int:professional_id>/", professional_detail, name="professional_detail"),
    path("professional_dashboard", professional_dashboard, name="professional_dashboard"),
    path('professional/dashboard/', views.professional_dashboard, name='professional_dashboard'),
    #path('login/', views.login_view, name='login'),
    path('professional/', views.professional_dashboard, name='professional_dashboard'),
    #path('regular_user.html', views.regular_user_dashboard, name='regular_user_dashboard'),
    path('professional_detail/', views.professional_detail, name='professional_detail'),  # No ID required

] 







    