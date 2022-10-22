from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Sale(models.Model):
    class PaymentMethodChoices(models.TextChoices):
        CASH = "CASH", "CASH"
        DEBIT = "DEBIT", "DEBIT"
        CREDIT = "CREDIT", "CREDIT"

    # Customer could be linked with a relational field if you have a database of customers
    customer_name = models.CharField(max_length=254)
    order_date = models.DateTimeField()
    quantity_of_items = models.IntegerField(validators=[MinValueValidator(1)])
    order_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(
        max_length=6,
        choices=PaymentMethodChoices.choices,
        default=PaymentMethodChoices.CASH,
    )
    # Delivery time in minutes
    delivery_time = models.IntegerField(validators=[MinValueValidator(1)])
    food_rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    delivery_rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )

    def __str__(self):
        return f"{self.customer_name}'s order"
