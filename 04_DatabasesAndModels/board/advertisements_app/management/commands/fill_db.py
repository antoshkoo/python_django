from django.core.management.base import BaseCommand
import uuid
from advertisements_app.models import Advertisement

class Command(BaseCommand):
    help = 'Наполнение базы случайными объявлениями'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Количество')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
           new_advertisement = Advertisement(title=uuid.uuid4(), description=i, status_id=1, type_id=1)
           new_advertisement.save()
