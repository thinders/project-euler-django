from django.urls import path

from . import views

urlpatterns = [path("problem/<int:num>/", views.problem, name="problem")]
