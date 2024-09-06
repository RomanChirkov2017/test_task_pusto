from django.db import models


class Player(models.Model):
    username = models.CharField(max_length=250, unique=True, verbose_name='Имя пользователя')
    first_login = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации пользователя')
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def assign_boost(self, boost_type, description):
        """ Метод для назначения буста пользователю. """

        Boost.objects.create(player=self, type=boost_type, description=description)


class Boost(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name='Игрок')
    type = models.CharField(max_length=100, verbose_name='Тип буста')
    description = models.TextField(verbose_name='Описание буста')
    date_of_receipt = models.DateTimeField(auto_now=True, verbose_name='Дата получения')

    def __str__(self):
        return f'{self.player} - {self.type}'

    class Meta:
        verbose_name = 'Буст'
        verbose_name_plural = 'Бусты'

