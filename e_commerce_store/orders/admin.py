from django.contrib import admin
from django.utils.html import mark_safe

from .models import Order, OrderItem

# Register your models here.


def order_payment(obj):
    url = obj.get_stripe_url()
    if obj.stripe_id:
        html = f'<a href="{url}" target="_blank">{obj.stripe_id}</a>'
        return mark_safe(html)
    return ""


order_payment.short_description = "Stripe payment"


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "paid", "created", "updated", order_payment]
    list_filter = ["paid", "created", "updated"]
    inlines = [OrderItemInline]
