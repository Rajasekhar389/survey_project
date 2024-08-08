from django.contrib import admin
from django.urls import path
from survey import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('survey/', views.survey, name='survey'),
]
