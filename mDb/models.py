from django.db import models

# Create your models here.
class  movie_data(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=False)
    released_year = models.IntegerField()
    ratings = models.FloatField()
    genres = models.CharField(max_length=10)

    def __str__(self):      
        return self.title

