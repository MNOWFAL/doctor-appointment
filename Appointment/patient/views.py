from django.shortcuts import render, redirect
from patient.forms import SignUpForm, AppointmentForm
from patient.models import Doctor, Appointment
from django.http import HttpResponse
import razorpay
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    doctors = Doctor.objects.all()
    return render(request, "index.html", {"doctors": doctors})


def user_register(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            user = fm.save(commit=False)
            user.set_password(fm.cleaned_data["password1"])
            user.save()
            return redirect("patient:login")
    else:
        fm = SignUpForm()
    return render(request, "register.html", {"form": fm})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect("patient:index")
        else:
            return HttpResponse("Invalid username or password. Please try again.")
    return render(request, "login.html")


@login_required(login_url="patient:login")
def user_logout(request):
    logout(request)
    return redirect("patient:login")


def appointment_view(request):
    doctors = Doctor.objects.all()
    if request.method == "POST":
        doctor_id = request.POST.get("doctor")
        if doctor_id:
            try:
                doctor = Doctor.objects.get(id=int(doctor_id))
                app_date = request.POST["app_date"]
                appointment = Appointment(name=doctor, app_date=app_date)
                appointment.save()
                return redirect("patient:appointment_success")
            except ValueError:
                return HttpResponse("Invalid doctor ID. Please try again.")
            except Doctor.DoesNotExist:
                return HttpResponse("Doctor not found. Please try again.")
        else:
            return HttpResponse("Please select a doctor.")
    else:
        appointment = AppointmentForm()
        return render(request, "appointment.html", {"doctors": doctors})


def appointment_success(request):
    appointments = Appointment.objects.all()
    return render(
        request,
        "appointment_success.html",
        {"appointments": appointments},
    )


def payment(request):
    return render(request, "payment.html")


# def payment(request):
#     if request.method == "POST":
#         amount = 500  # amount in paise
#         client = razorpay.Client(
#             auth=("YOUR_RAZORPAY_KEY_ID", "YOUR_RAZORPAY_KEY_SECRET")
#         )
#         payment = client.order.create(
#             {"amount": amount, "currency": "INR", "payment_capture": "1"}
#         )
#         return render(request, "payment.html", {"payment": payment})
#     return render(request, "payment.html")


# def payment_success(request):
#     if request.method == "POST":
#         payment_id = request.POST.get("razorpay_payment_id")
#         order_id = request.POST.get("razorpay_order_id")
#         signature = request.POST.get("razorpay_signature")
#         client = razorpay.Client(
#             auth=("YOUR_RAZORPAY_KEY_ID", "YOUR_RAZORPAY_KEY_SECRET")
#         )
#         params_dict = {
#             "razorpay_order_id": order_id,
#             "razorpay_payment_id": payment_id,
#             "razorpay_signature": signature,
#         }
#         try:
#             client.utility.verify_payment_signature(params_dict)
#             return HttpResponse("Payment successful!")
#         except:
#             return HttpResponse("Payment failed!")
#     return HttpResponse("Invalid request!")
