from django.db import models
from django.db.models import ForeignKey, TextField, CharField, EmailField, BooleanField, DateTimeField

from trainer.models import Trainer


# Create your models here.


class Feedback(models.Model):

    first_name = CharField(max_length=40)
    last_name = CharField(max_length=40)
    email = EmailField(max_length=40)
    trainer = ForeignKey(Trainer, on_delete=models.CASCADE, null=True)
    message = TextField(max_length=400)
    active = BooleanField(default=True)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} left a feedback for {self.trainer}'