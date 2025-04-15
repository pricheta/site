from django.urls import path

from . import chemistry_views, index_views, doctor_views

urlpatterns = [
    path('', index_views.index, name='index'),
    path('chemistry', chemistry_views.index, name='chemistry'),
    path('doctor', doctor_views.index, name='doctor'),
]

