from django.urls import path
from .views import checker, formInput

urlpatterns = [
    path('', checker, name='checker'),
    path('form-input/', formInput, name='formInput')
]