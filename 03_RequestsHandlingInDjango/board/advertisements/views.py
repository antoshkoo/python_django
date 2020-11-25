from django.http import HttpResponse
from django.shortcuts import render
# from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.views.generic.base import View

counter = 0


@method_decorator(csrf_exempt, name='dispatch')
class Advertisements(View):

    def get(self, request):
        advertisements = [
            'Мастер на час',
            'Выведение из запоя',
            'Услуги экскаватора-погрузчика, гидромолота, ямобура'
        ]
        advertisements_1 = [
            'Мастер на час',
            'Выведение из запоя',
            'Услуги экскаватора-погрузчика, гидромолота, ямобура'
        ]
        return render(request, 'advertisements/advertisement_list.html', {'adv': advertisements,
                                                                          'adv2': advertisements_1,
                                                                          'counter': counter})

    def post(self, request):
        global counter
        counter += 1
        return HttpResponse('Новая запись успешно добавлена.')


class About(TemplateView):
    template_name = 'advertisements/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Доска объявлений'
        context['description'] = 'Это та самая доска объявлений!'

        return context


class Contacts(TemplateView):
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['phone'] = '+7 (926) 098-7666'
        context['email'] = 'antoshkoo@gmail.com'
        context['address'] = 'г.Сочи, пгт Красная поляна, ул. ГЭС, д.4'

        return context


class Home(View):

    def get(self, request):
        form_choices_region = ['Москва', 'Санкт-Петербург', 'Казань', 'Новосибирск', 'Екатеринбург', 'Владивосток',
                               'Сочи']
        form_choices_category = ['Хобби', 'Транспорт', 'Недвижимость']

        return render(request, 'advertisements/home.html', {'choice_regions': form_choices_region,
                                                            'choice_categories': form_choices_category})
