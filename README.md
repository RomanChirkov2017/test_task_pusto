# Тестовое задание для бэкенд разработчика на Python

## Задания раздельные, в первой таске нужно просто описать модели.

### 1. Приложение подразумевает ежедневный вход пользователя, начисление баллов за вход. 
### Нужно отследить момент первого входа игрока для аналитики. Также у игрока имеются игровые бонусы в виде нескольких типов бустов. 
### Нужно описать модели игрока и бустов с возможностью начислять игроку бусты за прохождение уровней или вручную.


from django.db import models

class Player(models.Model):

    pass
    

class Boost(models.Model):

    pass


### 2. Дано несколько моделей

from django.db import models

class Player(models.Model):

    player_id = models.CharField(max_length=100)
    
    
class Level(models.Model):

    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    
    
    
class Prize(models.Model):

    title = models.CharField()
    
    
class PlayerLevel(models.Model):

    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    completed = models.DateField()
    is_completed = models.BooleanField(default=False)
    score = models.PositiveIntegerField(default=0)
    
    
class LevelPrize(models.Model):

    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE)
    received = models.DateField()
     

Написать два метода:

1) Присвоение игроку приза за прохождение уровня.
2) Выгрузку в csv следующих данных: id игрока, название уровня, пройден ли уровень, полученный приз за уровень. 
Учесть, что записей может быть 100 000 и более.

----------------------------------------------------------------------------------------------------------

# Задание #1

### В корневой директории проекта создано приложение game_profile, в котором в файле models.py описаны требуемые модели Player и Boost.
### В модели Player реализован метод assign_boost, который позволяет начислять игроку бусты.


# Задание #2

## Пункт 1:
### В корневой директории проекта создано приложение game_reward, в котором в файле models.py классу PlayerLevel добавлен метод assign_prize, 
### который отвечает за присвоение приза игроку после прохождения уровня.

## Пункт 2:
### В приложении game_reward создан файл services.py, в котором реализованы функции stream_csv_data и download_csv, 
### отвечающие за выгрузку в csv файл данных: id игрока, название уровня, пройден ли уровень, полученный приз за уровень.
### Функции реализованы с помощью класса StreamingHttpResponse, который позволяет эффективно обрабатывать большое количество данных.
