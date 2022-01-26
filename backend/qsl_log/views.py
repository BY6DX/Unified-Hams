from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import LogEntry

# Create your views here.
def QSLLogIndexView(request):
    template = loader.get_template('qsl_log/index.html')
    selected_log_entries = LogEntry.objects.all()

    context = {
        'log_entries': selected_log_entries
    }
    return HttpResponse(template.render(context, request))