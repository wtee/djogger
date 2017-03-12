from .models import Page

def pages(context):
    return {'pages': Page.objects.published()}