from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import *

def index(request):
    chasers = Chaser.objects.order_by('-pub_date')[:5]
    template = loader.get_template("chaser/index.html")
    context =  RequestContext(request, {
         'chasers': chasers,
    })
    return HttpResponse(template.render(context))

