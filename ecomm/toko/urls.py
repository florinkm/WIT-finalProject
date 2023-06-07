from django.urls import path
from . import views

app_name = 'toko'

urlpatterns = [
     path('', views.HomeListView.as_view(), name='home-produk-list'),
     path('product/<slug>/', views.ProductDetailView.as_view(), name='produk-detail'),
     path('checkout/', views.CheckoutView.as_view(), name='checkout'),
     path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
     path('remove_from_cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
     path('order-summary/', views.OrderSummaryView.as_view(), name='order-summary'),
     path('payment/<payment_method>', views.PaymentView.as_view(), name='payment'),
     path('paypal-return/', views.paypal_return, name='paypal-return'),
     path('paypal-cancel/', views.paypal_cancel, name='paypal-cancel'),
     path('detergent-laundry/',views.DetergentLaundryView.as_view(), name='detergent-laundry'),
     path('anti-noda/',views.AntiNodaView.as_view(), name='anti-noda'),
     path('pelengkap-laundry/',views.PelengkapLaundryView.as_view(), name='pelengkap-laundry'),
     path('mesin-laundry/',views.MesinLaundryView.as_view(), name='mesin-laundry'),
     path('search-result', views.SearchResultView.as_view(), name='search')
]
