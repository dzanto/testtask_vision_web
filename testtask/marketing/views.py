from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from.models import Card

# Create your views here.


def index(request):
    card1 = get_object_or_404(Card, name='card1')
    card2 = get_object_or_404(Card, name='card2')
    return render(request, 'index.html', {"card1": card1, 'card2': card2})

