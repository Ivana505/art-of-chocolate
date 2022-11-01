from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Contact Us"
            body = {
             'name': form.cleaned_data['name'],
             'email_address': form.cleaned_data['email_address'],
             'phone': form.cleaned_data['phone'],
             'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(
                    subject, message, 'admin@test.com', ['admin@test.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect("shop")

    form = ContactForm()
    return render(request, "contact/contact.html", {'form': form})
