from django.db import models


class DailyProfit(models.Model):
    date = models.DateField()
    profit = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.date}; {self.user} - {self.profit}"
