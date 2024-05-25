from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Halaman utama
    path('pemasukan/', views.pemasukan, name='pemasukan'), 
    path('pengeluaran/', views.pengeluaran, name='pengeluaran'), 
    path('add/', views.add_income, name='add'),  # Menambah data ke database
    path('update/<int:id>/', views.update_income, name='update'),  # Mengupdate data
    path('delete/<int:id>/', views.delete_income, name='delete'),  # Menghapus data
    path('add-outcome/', views.add_outcome, name='add_outcome'),  # Menambah data ke database
    path('update-outcome/<int:id>/', views.update_outcome, name='update_outcome'),  # Mengupdate data
    path('delete-outcome/<int:id>/', views.delete_outcome, name='delete_outcome'),  # Menghapus data
]
