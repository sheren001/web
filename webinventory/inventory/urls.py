from django.urls import path
from . import views

urlpatterns = [
    path('equipment-search/', views.equipment_search, name='equipment-search'),
    path('update-equipment/', views.update_equipment, name='update-equipment'),
    # Other URL patterns specific to the inventory app...
]
