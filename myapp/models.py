from django.db import models

class Book(models.Model):
	year=models.IntegerField()
	branch=models.CharField(max_length=20)
	subject_name=models.CharField(max_length=100)
	unit_name=models.CharField(max_length=100,default='')
	file=models.FileField(upload_to='books/pdfs/')

	def __str__(self):
		return self.subject_name

	def delete(self,*args,**kwargs):
		self.file.delete()
		super().delete(*args,**kwargs)

	

