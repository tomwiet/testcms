from django.db import models

# Create your models here.

class Question(models.Model):

    title = models.CharField(max_length=200)
    quest_text  = models.TextField('Treść pytania')
    answer1 = models.TextField('Odpowiedź 1')
    answer2 = models.TextField('Odpowiedź 2')
    answer3 = models.TextField('Odpowiedź 3')
    answer4 = models.TextField('Odpowiedź 4')
    corect = models.IntegerField('Poprawna jest odpowiedź nr:')

    def __str__(self):
        return self.quest_text
