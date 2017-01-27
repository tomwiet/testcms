from django.db import models

# Create your models here.

class Task(models.Model):

    title = models.CharField(max_length=200)
    questtext  = models.TextField()
    answer1 = models.TextField()
    answer2 = models.TextField()
    answer3 = models.TextField()
    answer4 = models.TextField()
    corect = models.IntegerField()

    def __unicode__ (self):
        return self.questtext
