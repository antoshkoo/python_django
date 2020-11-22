from django.http import HttpResponse

from django.views import View
import random


class ToDoView(View):

    def get(self, request, *args, **kwargs):

        todo_list = ['Установить python', 'Установить django', 'Запустить сервер', 'Порадоваться результату',
                     'Внимательно прочитать ДЗ', 'Подумать', 'Сделать красиво', 'Сдать домашку:)', 'Порадоваться']

        return HttpResponse(f'<ul>'
                            f'<li>{random.choice(todo_list)}</li>'
                            f'<li>{random.choice(todo_list)}</li>'
                            f'<li>{random.choice(todo_list)}</li>'
                            f'<li>{random.choice(todo_list)}</li>'
                            f'<li>{random.choice(todo_list)}</li>'
                            f'</ul>')
