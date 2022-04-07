from django.db import models


class Ai_one(models.Model):
    current = models.DecimalField(max_digits=50, decimal_places=6, verbose_name='current')
    sts = models.IntegerField(choices=((0, 0), (1, 1), (2, 2)))

    def __str__(self):
        return f'id: {self.id} current: {self.current} sts:{self.sts}'

class Ai_two(models.Model):
    current = models.DecimalField(max_digits=50, decimal_places=6, verbose_name='current')
    sts = models.IntegerField(choices=((0, 0), (1, 1), (2, 2)))

    def __str__(self):
        return f'id: {self.id} current: {self.current} sts:{self.sts}'


class Else(models.Model):
    pass