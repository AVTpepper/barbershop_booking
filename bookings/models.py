from django.db import models

class Barber(models.Model):
    name = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(help_text="Years of experience")

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    duration = models.DurationField(help_text="Duration of the service (e.g., 00:30:00 for 30 minutes)")
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.duration}) - {self.price} SEK"

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.customer_name} - {self.date} {self.time}"