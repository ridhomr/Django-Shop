from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from store.forms import ProdukForm, KategoriForm #FormLogin
from store.models import produk, kategoriProduk
from .forms import FormLogin
from django.contrib.auth import authenticate, login
#from .forms import FormLogin
# Create your views here.

def form(request):
	form = FormLogin()

	if request.method == 'POST':
		username_login = request.POST['username']
		password_login = request.POST['password']

		user = authenticate(request, username=username_login, password=password_login)

		if user is not None:
			login(request, user)
			return redirect('/belanja')
	return render(request, 'views/login.html',{'form': form})

def logoutView(request):
	if request.method == "POST":
		if request.POST['logout'] == "Submit":
			logout(request)
		return redirect("/login")
	return render(request, "views/login.html")

def index(request):
	return render(request, 'views/home.html')

def contact(request):
	return render(request, 'views/contact.html')

def registrasi(request):
	return render(request, 'views/registrasi.html')

def belanja(request):
	return render(request, 'views/belanja.html')

def about_arabian(request):
	return render(request, 'views/about.html')

def on_sale(request):
	if request.method == "POST":
		if request.POST['belanja'] == "Submit":
			belanja(request)
		return redirect("/belanja")
	return render(request, 'views/on_sale.html')

def all_produk(request):
	context = { 
		'produk': produk.objects.all()
	}
	return render(request, 'views/listproduk.html', context)

def all_produkA(request):
	context = { 
		'produk': produk.objects.all()
	}
	return render(request, 'views/produk.html', context)
	
def all_kategoriA(request):
	context = { 
		'kategori': kategoriProduk.objects.all()
	}
	return render(request, 'views/kategori.html',context)

def add_product_submit(request):
	if request.method == 'POST':
		form=ProdukForm(request.POST)
		if form.is_valid(): 
			form.save() 
		return redirect('adminpProduks')
	else: 
		form = ProdukForm()
	return render(request, 'views/produkForm.html',{'form': form})

def add_categori_submit(request):
	if request.method == 'POST':
		form=KategoriForm(request.POST)
		if form.is_valid(): 
			form.save() 
		return redirect('adminKategoris')
	else: 
		form = KategoriForm()
	return render(request, 'views/kategoriForm.html',{'form': form})

def add_categori(request):
	return render(request, 'views/kategoriForm.html')


# delete & update

def hapus_produk(request,id_produk):
	Produk=produk.objects.get(id=id_produk)
	Produk.delete()
	return redirect('adminpProduks')

def hapus_kategori(request,id_kategori):
	kategori=kategoriProduk.objects.get(id=id_kategori)
	kategori.delete()
	return redirect('adminKategoris')

def sunting_produk(request,id_produk):
	instance = get_object_or_404(produk, id=id_produk)
	form = ProdukForm(instance=instance)
	if form.is_valid():
		form.save(commit=False)
		return redirect('adminpProduks')
	return render(request, 'views/produkForm.html',{'form': form})

def sunting_kategori(request,id_kategori):
	instance = get_object_or_404(kategoriProduk, id=id_kategori)
	form = ProdukForm(instance=instance)
	if form.is_valid():
		form.save(commit=False)
		return redirect('adminKategoris')
	return render(request, 'views/kategoriForm.html',{'form': form})


# detail about
def detail_about(request):
	context = {
		'detail': detail_about,
	}
	return render(request, 'detail/detail_about.html', context)

def detail_parfum1(request):
	context = {
		'detail_parfum1': detail_parfum1,
	}
	return render(request, 'detail/detail_parfum1.html', context)

def detail_parfum2(request):
	context = {
		'detail_parfum2': detail_parfum2,
	}
	return render(request, 'detail/detail_parfum2.html', context)

def detail_parfum3(request):
	context = {
		'detail_parfum3': detail_parfum3,
	}
	return render(request, 'detail/detail_parfum3.html', context)

def detail_parfum4(request):
	context = {
		'detail_parfum4': detail_parfum4,
	}
	return render(request, 'detail/detail_parfum4.html', context)

def detail_parfum5(request):
	context = {
		'detail_parfum5': detail_parfum5,
	}
	return render(request, 'detail/detail_parfum5.html', context)

def detail_parfum6(request):
	context = {
		'detail_parfum6': detail_parfum6,
	}
	return render(request, 'detail/detail_parfum6.html', context)

def detail_parfum7(request):
	context = {
		'detail_parfum7': detail_parfum7,
	}
	return render(request, 'detail/detail_parfum7.html', context)

def detail_parfum8(request):
	context = {
		'detail_parfum8': detail_parfum8,
	}
	return render(request, 'detail/detail_parfum8.html', context)

def detail_parfum9(request):
	context = {
		'detail_parfum9': detail_parfum9,
	}
	return render(request, 'detail/detail_parfum9.html', context)

def detail_parfum10(request):
	context = {
		'detail_parfum10': detail_parfum10,
	}
	return render(request, 'detail/detail_parfum10.html', context)

def detail_parfum11(request):
	context = {
		'detail_parfum11': detail_parfum11,
	}
	return render(request, 'detail/detail_parfum11.html', context)

def detail_parfum12(request):
	context = {
		'detail_parfum12': detail_parfum12,
	}
	return render(request, 'detail/detail_parfum12.html', context)


# ADMIN
def detail_parfum1_admin(request):
	context = {
		'detail_parfum1_admin': detail_parfum1_admin,
	}
	return render(request, 'detail_produk_admin/detail_parfum1.html', context)

def detail_parfum2_admin(request):
	context = {
		'detail_parfum2_admin': detail_parfum2_admin,
	}
	return render(request, 'detail_produk_admin/detail_parfum2.html', context)

def detail_parfum3_admin(request):
	context = {
		'detail_parfum3_admin': detail_parfum3_admin,
	}
	return render(request, 'detail_produk_admin/detail_parfum3.html', context)

def detail_parfum4_admin(request):
	context = {
		'detail_parfum4_admin': detail_parfum4_admin,
	}
	return render(request, 'detail_produk_admin/detail_parfum4.html', context)

def detail_parfum5_admin(request):
	context = {
		'detail_parfum5_admin': detail_parfum5_admin,
	}
	return render(request, 'detail_produk_admin/detail_parfum5.html', context)

def detail_parfum6_admin(request):
	context = {
		'detail_parfum6_admin': detail_parfum6_admin,
	}
	return render(request, 'detail_produk_admin/detail_parfum6.html', context)

def detail_parfum7_admin(request):
	context = {
		'detail_parfum7_admin': detail_parfum7_admin,
	}
	return render(request, 'detail_produk_admin/detail_parfum7.html', context)

def detail_parfum8_admin(request):
	context = {
		'detail_parfum8_admin': detail_parfum8_admin,
	}
	return render(request, 'detail_produk_admin/detail_parfum8.html', context)

def detail_parfum9_admin(request):
	context = {
		'detail_parfum9_admin': detail_parfum9_admin,
	}
	return render(request, 'detail_produk_admin/detail_parfum9.html', context)

def detail_parfum10_admin(request):
	context = {
		'detail_parfum10_admin': detail_parfum10_admin,
	}
	return render(request, 'detail_produk_admin/detail_parfum10.html', context)

def detail_parfum11_admin(request):
	context = {
		'detail_parfum11_admin': detail_parfum11_admin,
	}
	return render(request, 'detail_produk_admin/detail_parfum11.html', context)

def detail_parfum12_admin(request):
	context = {
		'detail_parfum12_admin': detail_parfum12_admin,
	}
	return render(request, 'detail_produk_admin/detail_parfum12.html', context)