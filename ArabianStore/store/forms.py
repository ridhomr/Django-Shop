from django import forms
from store.models import produk,kategoriProduk

#login
from django.contrib.auth.models import User

class FormLogin(forms.Form):
	username = forms.CharField(widget=forms.TextInput(
					attrs={'placeholder': 'Username'})
				)
	password = forms.CharField(widget=forms.PasswordInput(
					attrs={'placeholder': 'Password'})
				)

class ProdukForm(forms.ModelForm):
	class Meta: 
		model = produk 

		fields= [ 
		'nama' ,
		'deskripsi',
		'harga' ,		
		'stok',
		'kategori',
		'status'

		]
		
		widget={
		'nama' : forms.TextInput(attrs={'class': 'form-control'}),
		'deskripsi':forms.TextInput(),
		'harga' : forms.FloatField(),
		'status': forms.widgets.CheckboxInput(),
		'stok': forms.IntegerField(),
		'kategori': forms.ModelChoiceField(queryset=kategoriProduk.objects.all()),
		}

class KategoriForm(forms.ModelForm):
	class Meta: 
		model = kategoriProduk 

		fields= [ 
		'nama' ,
		'deskripsi',
		]

		labels={
		'nama' : 'Nama',
		'deskripsi': 'Deskripsi',
		}

		
		widget={
		'nama' : forms.TextInput(),
		'deskripsi' : forms.TextInput(),
		}

		