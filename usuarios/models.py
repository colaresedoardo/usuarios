from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    apelido = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
