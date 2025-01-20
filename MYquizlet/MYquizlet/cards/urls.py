from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('card-set/<int:pk>/', views.card_set_detail, name='card_set_detail'),
    path('card/<int:pk>/', views.card_detail, name='card_detail'),
    path('card-set/new/', views.card_set_create, name='card_set_create'),
    path('card-set/<int:pk>/edit/', views.card_set_edit, name='card_set_edit'),
    path('card-set/<int:pk>/add-card/', views.add_card, name='add_card'),
    path('card/<int:pk>/edit/', views.edit_card, name='edit_card'),
    path('card/<int:pk>/delete/', views.delete_card, name='delete_card'),
    path('card-set/<int:pk>/add-review/', views.add_review, name='add_review'),
]
