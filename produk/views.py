from django.shortcuts import render, redirect, get_object_or_404
from .models import Produk
from .forms import ProdukForm
from .services import fetch_produk

def ambil_data(request):
    fetch_produk("username", "password")
    return redirect('produk_list')

def produk_list(request):
    produk = Produk.objects.all()
    return render(request, 'produk/list.html', {'produk': produk})

def produk_bisa_dijual(request):
    produk = Produk.objects.filter(
        status__nama_status__iexact="bisa dijual"
    )
    return render(request, 'produk/list.html', {'produk': produk})

def produk_tambah(request):
    form = ProdukForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('produk_list')
    return render(request, 'produk/form.html', {'form': form})

def produk_edit(request, id):
    produk = get_object_or_404(Produk, id=id)
    form = ProdukForm(request.POST or None, instance=produk)
    if form.is_valid():
        form.save()
        return redirect('produk_list')
    return render(request, 'produk/form.html', {'form': form})

def produk_hapus(request, id):
    produk = get_object_or_404(Produk, id=id)
    produk.delete()
    return redirect('produk_list')
