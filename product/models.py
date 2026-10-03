from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg, Count


class Product(models.Model):
    name = models.CharField("Name", max_length=200)
    price = models.PositiveIntegerField("Price")
    average_rating = models.FloatField("Average rating", default=0, editable=False)
    rating_count = models.PositiveIntegerField("Rating count", default=0, editable=False)

    def __str__(self):
        return self.name

    def update_rating(self):
        result = self.ratings.aggregate(avg=Avg("score"), cnt=Count("id"))
        self.average_rating = round(result["avg"] or 0, 2)
        self.rating_count = result["cnt"]
        self.save(update_fields=["average_rating", "rating_count"])


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ratings")
    score = models.PositiveSmallIntegerField(
        "Score", validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["product", "user"], name="unique_user_product_rating")
        ]

    def __str__(self):
        return f"{self.user} -> {self.product}: {self.score}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.product.update_rating()

    def delete(self, *args, **kwargs):
        product = self.product
        super().delete(*args, **kwargs)
        product.update_rating()