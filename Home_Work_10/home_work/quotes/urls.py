from django.urls import path

from . import views
from .views import AddAuthorView, AddQuoteView

app_name = "quotes"

urlpatterns = [
    path('', views.main, name="root"),
    path('<int:page>', views.main, name="root_paginate"),
    path('author/<id>', views.author_info, name="author_info"),
    path('add_author', AddAuthorView.as_view(), name="add_author"),
    path('add_quote', AddQuoteView.as_view(), name="add_quote")
]