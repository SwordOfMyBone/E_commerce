from django.shortcuts import get_object_or_404, render

from e_commerce_store.cart.forms import CartAddProductForm

from .models import Category, Product

# Create your views here.


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, is_available=True)
    cart_product_form = CartAddProductForm()
    return render(
        request,
        "store/product/detail.html",
        {"product": product, "cart_product_form": cart_product_form},
    )


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(
        request,
        "store/product/list.html",
        {"category": category, "categories": categories, "products": products},
    )
