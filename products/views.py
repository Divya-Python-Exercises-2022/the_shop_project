from django.http import HttpResponse
from django.shortcuts import render

from products.models import Products
# Create your views here.

def products_as_template(request):
    filters = request.GET.get('manufacturer', None)

    if filters is not None:
        context = {
            'products': Products.objects.filter(manufacturer__name__contains=filters),
            'filters': filters
        }
    else:
        context = {
            'products': Products.objects.all(),
            'filters': filters
        }

    return render(request, 'products.html',context)

    # Alternate way -- one line code
    #return render(request, 'products.html', {'products': Products.objects.all()})


def product_details(request, product_id):
    product = Products.objects.get(id=product_id)
    context = {
        'products':product
    }
    return render(request,'product_details.html', context)


def products_as_string(request):
    products_objs = Products.objects.all()

    list_of_items_str = '<ul>'

    for product in products_objs:
        list_of_items_str += f'<li>{product.name} - €{product.price}</li>'
    list_of_items_str += '</ul>'

    result = """
        <ul>
            <li>iPhone - 1000€ </li>
            <li>Samsung - 500€</li>
            <li>Motorola- 900€</li>
        </ul>
    """

    #return HttpResponse("<b>Hi!</b>")
    return HttpResponse(list_of_items_str)