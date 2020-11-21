from django.shortcuts import render, redirect
from .models import Pic, PIC_CHOICES, Text, TEXT_CHOICES
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from .forms import ContactForm

PIC_DICT = {a: None for a, b in PIC_CHOICES}
TEXT_DICT = {a: None for a, b in TEXT_CHOICES}


def index(request):
    pic_list = Pic.objects.all()
    for pic in pic_list:
        PIC_DICT[pic.name] = pic

    text_list = Text.objects.all()
    for text in text_list:
        TEXT_DICT[text.name] = text

    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail('Message from site', message,
                          from_email, ['manager@mysite.com'])
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('index')
    else:
        return HttpResponse('Неверный запрос.')

    return render(request, 'index.html', {
        'form': form,
        "PIC_DICT": PIC_DICT,
        "TEXT_DICT": TEXT_DICT,
    })
