"""WishList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from wishlist import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register_view ,name='register'),
    path('login/',views.login_view ,name='login'),
    path('logout/',views.logout_view ,name='logout'),

    path('home/', views.home_view, name='home'),
    path('home/list/', views.wishlist_list, name='wishlist-list'),
    path('home/list/?P<wishlist_id>[0-9a-f-]+/', views.wishlist_detail, name='wishlist-detail'),
    path('home/list/create/', views.wishlist_create, name='wishlist-create'),

    path('home/list/?P<wishlist_id>[0-9a-f-]+/delete/', views.wishlist_delete, name='wishlist-delete'),

    path('home/list/?P<wishlist_id>[0-9a-f-]+/item/add/', views.item_create, name='item-create'),
    path('home/list/?P<wishlist_id>[0-9a-f-]+/<int:item_id>/item/delete/', views.item_delete, name='item-delete'),
    path('home/list/?P<wishlist_id>[0-9a-f-]+/<int:item_id>/item/bought/', views.item_buy, name='item-buy'),

]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
