from django.db import models
from django.core.validators import validate_image_file_extension

class Hotel(models.Model):
    image=models.ImageField(upload_to='Hotel-Image',validators=[validate_image_file_extension])
    total_rooms = models.PositiveIntegerField(default=30)

    def __str__(self):
        return str(self.total_rooms)


class Booking(models.Model):
    booked=models.BooleanField(default=True)
    checkin_dtime=models.DateTimeField()
    checkout_dtime=models.DateTimeField()

    def __str__(self):
        return str(self.booked)

    class Meta:
        ordering = ['-booked']