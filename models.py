from django.db import models
class linhnhixinhdep(models.Model):
##    choiceDay = models.CharField(max_length=100)
##    choiceTime = models.IntegerField()
##    voterName = models.CharField(max_length=100)
    choiceDay = models.CharField(max_length=100)
    choiceTime = models.CharField(max_length=100)
    voterName = models.CharField(max_length=100)
    def __str__(self):
        return self.voterName
