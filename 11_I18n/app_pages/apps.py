from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppPagesConfig(AppConfig):
    name = 'app_pages'
    verbose_name = _('page')
    verbose_name_plural = _('pages')
