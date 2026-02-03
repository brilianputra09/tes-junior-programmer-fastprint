import requests
from .models import Produk, Kategori, Status

API_URL = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

def fetch_produk(username, password):
    response = requests.get(
        API_URL,
        auth=(username, password)
    )
    data = response.json()

    for item in data:
        kategori, _ = Kategori.objects.get_or_create(
            nama_kategori=item['kategori']
        )
        status, _ = Status.objects.get_or_create(
            nama_status=item['status']
        )

        Produk.objects.update_or_create(
            nama_produk=item['nama_produk'],
            defaults={
                'harga': item['harga'],
                'kategori': kategori,
                'status': status
            }
        )
