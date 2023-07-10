from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import CharField, TextInput, EmailField, EmailInput, \
    PasswordInput


class AuthorForm(UserCreationForm):
    fullname = CharField(max_length=150, required=True,
                           widget=TextInput(attrs={"class": "form-control"}))
    born_date = CharField(max_length=150, required=False,
                          widget=TextInput(attrs={"class": "form-control"}))
    born_location = CharField(max_length=150, required=False,
                       widget=TextInput(attrs={"class": "form-control"}))
    description = CharField(max_length=150, required=False,
                     widget=TextInput(attrs={"class": "form-control"}))
    quotes = CharField(max_length=150, required=False,
                          widget=TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("fullname", "born_date", "born_location", "description",
                  "quotes")


class QuotesForm(UserCreationForm):
    fullname = CharField(max_length=100, required=True,
                         widget=TextInput(attrs={"class": "form-control"}))
    quote = CharField(max_length=500, required=True,
                         widget=TextInput(attrs={"class": "form-control"}))
    tag = CharField(max_length=100, required=True,
                         widget=TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("fullname", "quote", "tag")


