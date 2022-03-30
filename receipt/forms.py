from django import forms
from .models import Receipt
import datetime

class ReceiptForm(forms.ModelForm):

    class Meta:
        model = Receipt
        fields = ['received_from', 'amount_in_words', 'payment_for', 'amount_in_figure', 'phone']

    def __init__(self, *args, **kwargs):
        super(ReceiptForm, self).__init__(*args,**kwargs)
        self.fields['received_from'].widget.attrs['placeholder'] = 'Received From'
        self.fields['amount_in_words'].widget.attrs['placeholder'] = 'Amount in words'
        self.fields['payment_for'].widget.attrs['placeholder'] = 'Payment for'
        self.fields['amount_in_figure'].widget.attrs['placeholder'] = 'Amount in figure'
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone Number'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'