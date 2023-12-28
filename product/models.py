from django.db import models
from django.utils.text import slugify


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return f"{self.category_name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)


class Product(models.Model):
    product_no = models.IntegerField()
    product_name = models.CharField(max_length=100, default="null name")
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='products/')
    slug = models.SlugField(unique=True, null=False, blank=True, db_index=True, editable=False)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_name}"

    def formatted_price(self):
        return "{:,.2f}".format(self.product_price)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)
