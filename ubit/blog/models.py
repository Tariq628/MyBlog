from django.db import models

# Create your models here.
class Blogpost(models.Model):
    image = models.ImageField(upload_to="blog/images", default="")
    heading = models.CharField(max_length=70, null=True)
    content = models.CharField(max_length=500, null=True)

    def __str__(self):
        return str(self.heading)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    textarea = models.CharField(max_length=600)

    def __str__(self):
        return self.name
    