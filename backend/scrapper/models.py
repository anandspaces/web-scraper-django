from django.db import models

# Create your models here.
class ScrappedModel(models.Model):
  url = models.URLField()
  content = models.TextField()
  created_at = models.DateTimeField(auto_add_now=True)

  def __str__(self):
    return self.url