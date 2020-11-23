from django.http import HttpResponse

from django.views import View
import random


class ToDoView(View):

    def get(self, request, *args, **kwargs):

        todo_list = ['Установить python', 'Установить django', 'Запустить сервер', 'Порадоваться результату',
                     'Внимательно прочитать ДЗ', 'Подумать', 'Сделать красиво', 'Сдать домашку:)', 'Порадоваться']
        # Я бы передал итерируемый объект если б не <ul></ul>, c ними нашел как сделать с помощью стриминга.
        # Но это мне показалось слишком сложным вариантом для такой задачи:)
        responce = HttpResponse()
        responce.write('<ul>')
        for i in range(5):
            responce.write(f'<li>{random.choice(todo_list)}</li>')
        responce.write('</ul>')
        return responce

