from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class CptData(models.Model):
    depth = models.FloatField()
    qc = models.FloatField()
    fs = models.FloatField()

    def __str__(self):
        return f"{self.depth} - QC: {self.qc}, FS: {self.fs}"
