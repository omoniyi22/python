from django import forms
from .models import Student

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and Student.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered")
        return email