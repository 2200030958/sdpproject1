from django.db import models


# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=1000)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    phonenumber = models.PositiveBigIntegerField()

    class Meta:
        db_table = "Register"


from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=20)
    comments = models.TextField()

    def __str__(self):
        return self.name  # You can choose any field to represent the model in a human-readable way
