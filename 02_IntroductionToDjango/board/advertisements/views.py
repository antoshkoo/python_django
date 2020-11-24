from django.shortcuts import render


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


def contacts(request, *args, **kwargs):
    return render(request, 'advertisements/contacts.html', {'phone': '8-800-708-19-45', 'email': 'sales@company.com'})


def about(request, *args, **kwargs):
    return render(request, 'advertisements/about.html', {'name': 'Бесплатные объявления',
                                                         'description': 'Бесплатные объявления в вашем городе!'})


def categories(request, *args, **kwargs):
    categories = ['Личные вещи',
                  'Транспорт',
                  'Хобби и отдых']
    return render(request, 'advertisements/categories.html', {'categories': categories})


def regions(request, *args, **kwargs):
    regions = ['Москва',
               'Казань',
               'Новосибирск',
               'Владивосток',
               'Сочи']
    return render(request, 'advertisements/regions.html', {'regions': regions})
