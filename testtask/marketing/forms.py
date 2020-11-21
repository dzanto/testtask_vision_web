from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Email', required=True)
    message = forms.CharField(label='Сообщение', required=True)