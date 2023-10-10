from django.db import models


class Messages(models.Model):
	email = models.EmailField()
	name = models.CharField(max_length=200)
	discord = models.CharField(max_length=200, blank=True, null=True)
	message = models.TextField(max_length=500)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'Remitent: {self.email} | Message: {self.message}'
