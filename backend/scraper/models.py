from django.db import models

# Create your models here.
class ScrapedModel(models.Model):
  url = models.URLField()
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.url