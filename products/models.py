from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    frontend_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_frontend_name(self):
        return self.frontend_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_rating(self):
        total = sum(int(review['stars']) for review in self.reviews.values())

        return total / self.reviews.count()

# thanks for video walk thru https://www.youtube.com/watch?v=Y5vvGQyHtpM


class ProductReview(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)

    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()

    date_added = models.DateTimeField(auto_now_add=True)
