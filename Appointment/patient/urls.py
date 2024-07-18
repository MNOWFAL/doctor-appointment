from django.urls import path
from . import views

app_name = "patient"

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.user_register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("appointment/", views.appointment_view, name="appointment"),
    path(
        "appointment_success/",
        views.appointment_success,
        name="appointment_success",
    ),
    path("payment/", views.payment, name="payment"),
    # path('payment/success/', views.payment_success, name='payment_success'),
]
