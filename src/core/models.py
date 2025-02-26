from django.db import models
from src.services.customer.models import Customer


class BillingAddress(models.Model):
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, related_name="billing_address"
    )
    attention = models.CharField(max_length=100, blank=True)
    country_region = models.CharField(max_length=100)
    street_1 = models.CharField(max_length=100)
    street_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    phone = models.IntegerField(blank=True)
    fax = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.customer.get_full_name} - Billing - {self.city}, {self.state}"
