from django.shortcuts import render

# Create your views here.


def newclient(request):
    #add a new topic
    if request.method != 'POST':
        #create a blank form
        form = ClientForm()
        
    else:
            form = ClientForm(request.POST)
            if form.is_valid():
                form.save()
                
            
    context = {'form':form}
    return render(request,'trucks/newclient.html',context)
