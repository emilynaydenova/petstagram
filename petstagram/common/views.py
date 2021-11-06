from django.shortcuts import render


# Create your views here.
from common.models import Comment


def landing_page(request):
    return render(request, 'landing_page.html')

