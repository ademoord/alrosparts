from django.db import models

# Create your models here.
class tbProjekte(models.Model):
	projTitle = models.CharField(max_length=200)
	projDesc = models.TextField()
	projCreated = models.DateTimeField("date published")
	projAuthor = models.CharField(max_length=60)

def __str__(self):
  	return self.projTitle

class tbComponent(models.Model):
    compName = models.CharField(max_length=60)
    compTotal = models.SmallIntegerField()
    compDesc = models.CharField(max_length=60)
    compPackage = models.CharField(max_length=20)
    compDist = models.CharField(max_length=20)
    compPartNum = models.CharField(max_length=40)

    def __str__(self):
    	return self.compName

class tbUnitTest(models.Model):
    testName = models.CharField(max_length=60)
    testDesc = models.CharField(max_length=60)
    testUnit = models.SmallIntegerField()

    def __str__(self):
        return self.testName
