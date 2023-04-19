from django import forms
from .models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "summary",
            "description",
            "location",
            "evidence",
            "type",
        ]
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Given name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Family name",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email address you check regularly",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Phone number we can reach you at",
                }
            ),
            "summary": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Write a one-line summary of the issue",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please describe the issue in as much detail as possible",
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please provide the estimated location of where this issue is",
                }
            ),
            "type": forms.Select(attrs={"class": "form-control"}),
        }