from django.db import models

# Create your models here.
class kategoriProduk(models.Model):
	nama = models.CharField(max_length=50)
	deskripsi = models.TextField(max_length=400)

class produk(models.Model):
	nama = models.CharField(max_length=100)
	deskripsi = models.TextField(max_length=300)
	status = models.BooleanField(default=True)
	harga = models.DecimalField(max_digits=6,decimal_places=2)
	stok = models.IntegerField()
	kategori = models.ForeignKey(kategoriProduk,null=True,blank=True, on_delete=models.DO_NOTHING)
