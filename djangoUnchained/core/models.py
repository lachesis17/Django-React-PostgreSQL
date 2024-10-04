from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class CptData(models.Model):
    depth = models.FloatField()
    qc = models.FloatField(null=True)
    fs = models.FloatField(null=True)
    u = models.FloatField(null=True)

    def __str__(self):
        return f"{self.depth} - QC: {self.qc}, FS: {self.fs}, U: {self.u}"
