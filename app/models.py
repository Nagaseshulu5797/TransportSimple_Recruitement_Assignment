from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse
class Quetions(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    quetion=models.CharField(max_length=100)

    def __str__(self):
        return self.quetion
    def get_absolute_url(self):
        return reverse('detail_info',kwargs={'pk':self.pk})

class Answers(models.Model):
    quetion=models.ForeignKey(Quetions, on_delete=models.CASCADE,related_name='scl')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    answer=models.CharField(max_length=100)

