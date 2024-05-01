from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    # Used for query acceleration, can be used to improve memory usage and for faster lookups in our DB table
    slug = models.SlugField(max_length=250, unique=True)
    # to get a particular category, similar to a route in url

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('list-category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='un-branded')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])
