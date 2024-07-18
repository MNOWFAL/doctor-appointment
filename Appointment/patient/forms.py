from django import forms
import datetime
from django.contrib.auth.models import User
from .models import Appointment


class SignUpForm(forms.ModelForm):
    phone = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "(xxx)xxx-xxxx",
                "oninput": "this.value = this.value.replace(/[^0-9.]/g, '');",
            }
        ),
    )
    dateofbirth = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), required=True
    )
    GENDER_CHOICES = [("M", "Male"), ("F", "Female"), ("O", "Other")]
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect(),
        required=True,
        help_text="Gender",
    )
    address = forms.CharField(max_length=250)
    COUNTRY_CHOICES = [
        ("IND", "India"),
        ("KSA", "Saudi Arebia"),
        ("US", "United States"),
        ("CA", "Canada"),
        ("UK", "United Kingdom"),
        ("AU", "Australia"),
    ]
    country = forms.ChoiceField(
        choices=COUNTRY_CHOICES,
        widget=forms.Select,
        required=True,
    )

    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    pincode = forms.CharField(
        max_length=6,
        required=True,
        widget=forms.TextInput(
            attrs={
                "oninput": "this.value = this.value.replace(/[^0-9.]/g, '');",
            }
        ),
    )

    password1 = forms.CharField(max_length=200, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=200, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "phone",
            "dateofbirth",
            "gender",
            "address",
            "country",
            "city",
            "state",
            "pincode",
            "password1",
            "password2",
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class RestrictedDateInput(forms.DateInput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs["min"] = datetime.date.today().strftime("%Y-%m-%d")
        self.attrs["max"] = (
            datetime.date.today() + datetime.timedelta(days=30)
        ).strftime("%Y-%m-%d")


class AppointmentForm(forms.ModelForm):
    app_date = forms.DateField(widget=RestrictedDateInput(attrs={"type": "date"}))

    class Meta:
        model = Appointment
        fields = ("name", "app_date", "token_no", "status")
