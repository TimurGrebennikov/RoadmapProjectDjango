from django.urls import path
from api.v1.payment import views as payment_views

urlpatterns = [
    path('payments/', payment_views.payment_list, name='payment_list'),
]