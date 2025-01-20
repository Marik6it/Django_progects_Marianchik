from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied


from django.db.models import Avg

class CardSet(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)   # Поле для зберігання рейтингу

    def calculate_rating(self):
        reviews = self.reviews.all()
        self.rating = reviews.aggregate(models.Avg('rating'))['rating__avg'] or 0
        self.save()


    def __str__(self):
        return self.name

    def check_owner(self, user):
        if self.owner != user:
            raise PermissionDenied


class Card(models.Model):
    term = models.CharField(max_length=200)
    definition = models.TextField()
    card_set = models.ForeignKey(CardSet, on_delete=models.CASCADE, related_name='cards')

    def __str__(self):
        return self.term
class Review(models.Model):
    card_set = models.ForeignKey(CardSet, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])  # Оцінка 1-5
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.rating} з 5"
