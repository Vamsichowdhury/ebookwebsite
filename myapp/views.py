from django.shortcuts import render,redirect
from . models import Book
from . forms import BookForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

def home(request):
	username=None
	if request.user.is_authenticated:
		username=request.user.username
	return render(request,'home.html',{"name":username})

def books_list(request):
	books=Book.objects.all()
	return render (request,'books_list.html',{"books":books})


def upload_book(request):
	if request.method=='POST':
		form=BookForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect("/myapp/books/")
	else:
		form=BookForm()

	return render(request,"upload_book.html",{"form":form})


def login_user(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect("/myapp/")
		else:
			redirect('/myapp/login/')
	return render(request,'login_user.html')

def logout_user(request):
	logout(request)
	return redirect("/myapp/")

def register_user(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)#collect all entered information from user
		if form.is_valid():
			username=form.cleaned_data['username']
			password1=form.cleaned_data['password1']
			form.save()
			return redirect("/myapp/login/")
	else:
		form=UserCreationForm()
	return render(request,'register_user.html',{"form":form})

def delete_book(request,pk):
	book=Book.objects.get(pk=pk)
	book.delete()
	return redirect('/myapp/books/')