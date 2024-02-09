from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class taskData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=30)
    desc = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    class Meta():
        db_table="Todo"

    def __str__(self):
        return self.task