from django.shortcuts import render

from clients.models import Clients, Address


# Create your views here.
def client(request):
    client = Clients.objects.all()
    context = {
        'clients': client
    }
    return render(request, 'clients.html',context)

def client_details(request, client_id):
    client = Clients.objects.get(id=client_id)
    context = {
        'client_details': client,
        'addresses': client.addresses.all()
    }
    return render(request, 'client_details.html', context)