from django.conf import settings

def base_data(request):
    base_context = {}
    base_context['SITE_DOMAIN_NAME'] = settings.SITE_DOMAIN_NAME
    base_context['BASE_TEMPLATE_DIR'] = settings.BASE_TEMPLATE_DIR
    return base_context