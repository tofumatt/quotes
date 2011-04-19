from django.conf import settings


def django_conf(request):
    return {
        'MEDIA_URL': settings.MEDIA_URL,
        'SITE_URL': settings.SITE_URL,
        'settings': settings,
    }
