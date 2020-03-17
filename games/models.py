from django.db import models


class Game(models.Model):

    def __str__(self):
        return self.name + '-' + self.game_type + '-' + self.price



    name = models.CharField(max_length=1000)
    game_type=models.CharField(max_length=1000)
    price = models.CharField(max_length=1000)
    game_img = models.CharField(max_length=1000)
