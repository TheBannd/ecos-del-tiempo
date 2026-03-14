from django.urls import path
from . import views
from .views import (
    PageListView,
    PageDetailView,
    PageCreateView,
    PageUpdateView,
    PageDeleteView,
)

urlpatterns = [

    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),

    # LISTA DE PAGES
    path('pages/', PageListView.as_view(), name='pages'),

    # CRUD
    path('pages/create/', PageCreateView.as_view(), name='page_create'),
    path('pages/edit/<int:pk>/', PageUpdateView.as_view(), name='page_edit'),
    path('pages/delete/<int:pk>/', PageDeleteView.as_view(), name='page_delete'),

    # DETALLE (SIEMPRE AL FINAL)
    path('pages/<int:pk>/', PageDetailView.as_view(), name='page_detail'),

]