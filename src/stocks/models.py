from django.db import models

from users.models import Profile


class DailyProfit(models.Model):
    date = models.DateField()
    profit = models.FloatField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.date}; {self.user} - {self.profit}"
