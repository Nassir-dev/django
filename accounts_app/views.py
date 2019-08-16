from django.shortcuts import render

# Create your views here.

def invoice(request):
    #create a new message 
    if request.method != 'POST':
    #create a blank form

        form = InvoiceForm()

    else:
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'trucks/create_invoice.html', context)

