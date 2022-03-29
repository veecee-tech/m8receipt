from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from receipt.forms import ReceiptForm
from receipt.models import Receipt

# Create your views here.

@login_required(login_url='login')
def generate_receipt(request):

    if request.method == 'POST':
        form = ReceiptForm(request.POST)

        if form.is_valid():
          
            form.save()


            return redirect('receipts')
    else:
        form = ReceiptForm()
    context = {
        'form': form
    }
    return render(request, 'receipt-form.html', context)

@login_required(login_url='login')
def all_receipts(request):

    receipts = Receipt.objects.all().order_by('-created_at')
        
    context = {
        'receipts': receipts
    }

    return render(request, 'all-receipts.html', context)

def single_receipt(request, id, receipt_no):

    single_receipt = get_object_or_404(Receipt, id = id, receipt_no = receipt_no)

    context = {
        'single_receipt': single_receipt
    }
    return render(request, 'index.html', context)



