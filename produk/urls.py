from django.urls import path
from . import views

urlpatterns = [
    path('', views.produk_list, name='produk_list'),
    path('ambil/', views.ambil_data, name='ambil_data'),
    path('bisa-dijual/', views.produk_bisa_dijual, name='bisa_dijual'),
    path('tambah/', views.produk_tambah, name='tambah'),
    path('edit/<int:id>/', views.produk_edit, name='edit'),
    path('hapus/<int:id>/', views.produk_hapus, name='hapus'),
]
