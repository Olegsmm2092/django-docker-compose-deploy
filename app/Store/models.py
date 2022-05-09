from django.db import models

class eBook(models.Model):
    name = models.CharField(max_length=51)
    price = models.FloatField()
    img_url = models.CharField(max_length=2048)

    def __str__(self):
        return self.title
