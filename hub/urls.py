from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.hub, name='hub'),
    path("hub/explorer", views.explorer, name='explorer'),
    path('hub/form/', views.form, name='form'),
    path('hub/create/', views.create, name='create'),
    path('hub/detalhe/<int:pk>/', views.detalhe, name="detalhe"),
    path('hub/update/<int:pk>/', views.update, name="update"),
    path('hub/delete/<int:pk>/', views.delete, name="delete"),
    path('hub/edit/<int:pk>/', views.edit, name="edit"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)