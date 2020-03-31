from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orderplaced/',views.orderplaced),
    path('restaurant/',views.restuarent,name='restuarant'),
    path('register/user/',views.customerRegister,name='register'),
    path('login/user/',views.customerLogin,name='login'),


    path('restlogin/restaurant/',views.restLogin,name='rlogin'),
    path('register/restaurant/',views.restRegister,name='rregister'),
    path('profile/restaurant/',views.restaurantProfile,name='rprofile'),
    path('profile/user/',views.customerProfile,name='profile'),
    path('user/create/',views.createCustomer,name='ccreate'),
    path('user/update/<int:id>/',views.updateCustomer,name='cupdate'),
    path('restaurant/create/',views.createRestaurant,name='rcreate'),
    path('restaurant/update/<int:id>/',views.updateRestaurant,name='rupdate'),
    path('restaurant/orderlist/',views.orderlist,name='orderlist'),
    path('restaurant/menu/',views.menuManipulation,name='mmenu'),
    path('logout/',views.Logout,name='logout'),
    path('restaurant/<int:pk>/',views.restuarantMenu,name='menu'),
    path('checkout/',views.checkout,name='checkout'),


    path('rest1login/restaurant1/',views.rest1Login,name='r1login'),
    path('profile/restaurant1/',views.restaurant1Profile,name='r1profile'),
    path('register/restaurant1/',views.rest1Register,name='r1register'),
    path('restaurant1/create/',views.createRestaurant1,name='r1create'),
    path('restaurant1/update/<int:id>/',views.updateRestaurant1,name='r1update'),
    path('restaurant1/',views.restuarent1,name='restuarant1'),

]