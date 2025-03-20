from django.db import models

# Create your models here.
class Recipe(models.Model): # visualizar isso como se fosse uma tabela sql
      title = models.CharField(max_length=65) # varchar
      description = models.CharField(max_length=165)
      slug = models.models.SlugField()
      preparation_time = models.IntegerField()
      preparation_time_uni = models.CharField(max_length=65)
      servings_time = models.IntegerField()
      servings_time_uni = models.CharField(max_length=65)
      preparation_steps = models.TextField()
      preparation_steps_is_html = models.BooleanField(default=False)
      created_at = models.DateField(auto_now_add=True) # vai pegar a data automaticamente
      update_at = models.DateField(auto_now=True)
      is_published = models.BooleanField(default=False)
      cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')


      pass