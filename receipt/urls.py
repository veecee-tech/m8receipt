from unicodedata import name
from django.urls import path
from receipt.views import *

urlpatterns = [
    path('receiptform/', generate_receipt, name = 'gen_receipt'),
    path('receipts/', all_receipts, name = 'receipts'),
    path('receipt/<int:id>/<str:receipt_no>/', single_receipt, name='single_receipt')
]
