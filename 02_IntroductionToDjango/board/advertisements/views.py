from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


def advertisements_list(request, *args, **kwargs):
    adv_personal = ['Крепления Union Force 2021', 'Кеды Converse', 'Кальян DSH']
    adv_transport = ['Mazda 6', 'Самокат детский', 'Шины']
    adv_hobby = ['Велосипед', 'Монополия', 'Лонгборд']
    return render(request, 'advertisements/advertisements_list.html', {'adv_personal': adv_personal,
                                                                       'adv_transport': adv_transport,
                                                                       'adv_hobby': adv_hobby})


def advertisement_1(request, *args, **kwargs):
    return render(request, 'advertisements/advertisement_1.html', {})


def advertisement_2(request, *args, **kwargs):
    return render(request, 'advertisements/advertisement_2.html', {})


def advertisement_3(request, *args, **kwargs):
    return render(request, 'advertisements/advertisement_3.html', {})


def advertisement_4(request, *args, **kwargs):
    return render(request, 'advertisements/advertisement_4.html', {})


def advertisement_5(request, *args, **kwargs):
    return render(request, 'advertisements/advertisement_5.html', {})


class Contacts(TemplateView):
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['phone'] = '8-800-708-19-45'
        context['email'] = 'sales@company.com'

        return context


class About(TemplateView):
    template_name = 'advertisements/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Бесплатные объявления'
        context['description'] = 'Бесплатные объявления в вашем городе!'

        return context


def categories(request, *args, **kwargs):
    categories = ['Личные вещи',
                  'Транспорт',
                  'Хобби и отдых']
    return render(request, 'advertisements/categories.html', {'categories': categories})


class Regions(View):

    def get(self, request):
        regions = ['Москва',
                   'Казань',
                   'Новосибирск',
                   'Владивосток',
                   'Сочи']
        return render(request, 'advertisements/regions.html', {'regions': regions})

    def post(self, request):
        return HttpResponse('Region created')
