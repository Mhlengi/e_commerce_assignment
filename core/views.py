from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST
from core.models import Cart, Product
from core.forms import CartAddProductForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def product_list(request):
    products = Product.objects.filter(available=True)
    return render(
        request,
        'core/product_list.html',
        {
            'products': products
         }
    )


def product_detail(request, id, slug):
    product = get_object_or_404(
        Product,
        id=id,
        slug=slug,
        available=True)
    cart_product_form = CartAddProductForm()
    return render(
        request,
        'core/product_detail.html',
        {
            'product': product,
            'cart_product_form': cart_product_form
         }
    )


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        return redirect('cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'core/product_detail.html', {'cart': cart})
