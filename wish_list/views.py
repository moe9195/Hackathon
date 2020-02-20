from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, ItemForm, WishlistForm, BoughtForm
from django.contrib.auth import login, logout, authenticate
from .models import Wishlist, Item
from django.contrib.auth.models import User
import json

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect("home")
    context = {
        "form":form,
    }
    return render(request, 'register.html', context)

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('wishlist-list')
    context = {
        "form":form
    }
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def wishlist_list(request):
    #wishlists = Wishlist.objects.all()
    wishlists = Wishlist.objects.filter(owner=request.user)
    context = {
    	"wishlists": wishlists,
    }
    return render(request, 'wishlist_list.html', context)

def wishlist_delete(request, wishlist_id):
    Wishlist.objects.get(id=wishlist_id).delete()
    return redirect('wishlist-list')

def wishlist_detail(request, wishlist_id):
    wishlist = Wishlist.objects.get(id=wishlist_id)
    items = wishlist.item_set.all().order_by("-date")
    context = {
        "wishlist": wishlist,
        "items": items,
    }
    return render(request, 'wishlist_detail.html', context)

def wishlist_create(request):
    form = WishlistForm()
    if request.user.is_anonymous:
        return redirect('signin')
    if request.method == "POST":
        form = WishlistForm(request.POST, request.FILES or None)
    if form.is_valid():
    	wishlist = form.save(commit=False)
    	wishlist.owner = request.user
    	wishlist.save()
    	return redirect('wishlist-list')
    context = {
        "form": form,
    }
    return render(request, 'create_wishlist.html', context)


def home_view(request):
    wishlists = Wishlist.objects.all()
    context = {
        "wishlists": wishlists,
        "msg": 'Create Your Wishlist'
    }
    return render(request, 'home.html', context)

def item_create(request, wishlist_id):
    wishlist = Wishlist.objects.get(id=wishlist_id)
    form = ItemForm()
    if request.user.is_anonymous:
        return redirect("login")
    if request.user != wishlist.owner:
    	return redirect("login")
    if request.method == "POST":
    	form = ItemForm(request.POST, request.FILES)
    	if form.is_valid():
            item = form.save(commit=False)
            item.wishlist = wishlist
            item.save()
            return redirect('wishlist-detail', wishlist_id)
    context = {
        "form":form,
        "wishlist": wishlist,
    }
    return render(request, 'create_item.html', context)

def item_delete(request, wishlist_id, item_id):
    wishlist = Wishlist.objects.get(id=wishlist_id)
    if request.user.is_anonymous:
        return redirect("wishlist-detail", wishlist_id)
    if request.user != wishlist.owner:
        return redirect("wishlist-detail", wishlist_id)
    Item.objects.get(id=item_id).delete()
    return redirect("wishlist-detail", wishlist_id)

def item_buy(request, wishlist_id, item_id):
    wishlist = Wishlist.objects.get(id=wishlist_id)
    item = Item.objects.get(id=item_id)
    if not item.checkbox:
        item.checkbox = True
        item.save()
        if request.user.is_anonymous:
            item.boughtby = "Anonymous"
            item.save()
        else:
            first = request.user.first_name
            if len(first) == 0:
                item.boughtby = request.user.username
            else:
                last = request.user.last_name
                item.boughtby = first + ' ' + last
                item.save()
    else:
        item.checkbox = False
        item.save()
    return redirect("wishlist-detail", wishlist_id)
