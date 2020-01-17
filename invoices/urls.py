from django.urls import path
from invoices import views

urlpatterns = [
    path('invoices',views.invoice_list),
    path('invoices/<int:pk>',views.invoice_detail),
]
