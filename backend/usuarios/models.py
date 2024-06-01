from django.db import models

class Usuario(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    senha = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.email
