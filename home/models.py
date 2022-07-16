from django.db import models

# Create your models here.
# python manage.py makemigration --->to create changes
# python manage.py migrate --->> apply the pending changes

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name