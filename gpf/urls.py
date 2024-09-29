# gpf/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('gpf-form/', views.gpf_form_view, name='gpf_form'),
    path('add-nominee/<int:gpf_form_id>/', views.add_nominee_view, name='add_nominee'),
    path('download-pdf/<int:gpf_form_id>/', views.download_pdf_view, name='download_pdf'),

]

