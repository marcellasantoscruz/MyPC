from django.db import models

class ProcessadorIniciante(models.Model):
    pergunta = models.TextField()
    alternativa_1 = models.TextField()
    alternativa_2 = models.TextField()
    alternativa_3 = models.TextField()
    alternativa_4 = models.TextField()
    resposta = models.TextField()

    def __str__(self):
        return self.pergunta