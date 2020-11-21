from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404
from.models import Pic, PIC_CHOICES, Text, TEXT_CHOICES
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
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
            # subject = request.POST.get('subject', '')
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

    # def success_view(request):
    #     return HttpResponse('Приняли! Спасибо за вашу заявку.')

