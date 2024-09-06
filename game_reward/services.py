import csv
from django.http import StreamingHttpResponse

from game_reward.models import PlayerLevel


class Echo:
    """ Эхо-объект, реализующий метод write, который просто возвращает значение, а не записывает его в файл. """

    def write(self, value):
        return value


def stream_csv_data():
    """ Генератор строк CSV. """

    yield ['Player ID', 'Level Title', 'Is Completed', 'Prize Title']

    for pl in PlayerLevel.objects.all().select_related('player', 'level').prefetch_related('level__levelprize_set'):
        for lp in pl.level.levelprize_set.all():
            yield [pl.player.player_id, pl.level.title, pl.is_completed, lp.prize.title]


def download_csv(request):
    """ Представление, которое возвращает CSV файл для скачивания. """

    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    response = StreamingHttpResponse((writer.writerow(row) for row in stream_csv_data()), content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="players_levels.csv"'
    return response