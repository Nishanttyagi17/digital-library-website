
from django.db import models


class Notes(models.Model):
    title = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    Branch = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='notes/pdfs/')
    

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)