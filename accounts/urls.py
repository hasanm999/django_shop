from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [

    path('register/', views.register, name='register'),

    path('register/otp/', views.register_otp, name='register_otp'),

    path('login/', views.login_view, name='login'),

    path('login/otp/', views.login_otp, name='login_otp'),

    path('profile/', views.profile, name='profile'),

    path('logout/', views.logout_view, name='logout'),
    path('create_ticket/', views.create_ticket, name='create-ticket'),
    path('ticket/list/', views.ticket_list, name='ticket-list'),
    path("ticket/detail/<int:ticket_id>", views.ticket_detail, name='ticket-detail'),
    path("resend_code/", views.resend_otp, name="resend_code"),
]
