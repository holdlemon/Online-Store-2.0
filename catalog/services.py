from django.core.cache import cache
from catalog.models import Product


def products_by_category(category_id):

    products = cache.get(f"products/category/{category_id}")
    if products:
        return products
    products = Product.objects.filter(category_id=category_id, is_published=True)
    cache.set(f"products/category/{category_id}", products, 60)
    return products
