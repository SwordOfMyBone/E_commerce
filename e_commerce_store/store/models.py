from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    """
    Category model for E-commerce store.
    """

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse("store:product_list_by_category", args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product model for E-commerce store.
    One-to-many relationship with Category.
    """

    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-time_created"]),
        ]

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.id, self.slug])

    def __str__(self):
        return self.name
