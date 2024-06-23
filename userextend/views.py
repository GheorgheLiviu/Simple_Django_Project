import random
from datetime import datetime

from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

from djangoProject.settings import EMAIL_HOST_USER
from userextend.forms import UserForm
from userextend.models import History


# Create your views here.


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            # Atribui valoarea new_user.first_name.title() campului first_name al obiectului new_user
            new_user.first_name = new_user.first_name.title()
            new_user.last_name = new_user.last_name.title()
            new_user.email = new_user.email.lower()

            # 1. Eliminati(comentati) campul username din forms.py (userextend)
            # 2. Usernameul sa fie compus din prima litera din first_name + last_name+_+6 cifre generate random
            # ex:. hscurtu_123456

            # new_user.username = new_user.first_name[0]+new_user.last_name+'_'+random.randint(100000,999999)
            new_user.username = f'{new_user.first_name[0].lower()}{new_user.last_name.lower().replace(" ", "")}_{random.randint(100000, 999999)}'
            new_user.save()

            # History

            get_message = (f'User-ul a fost adaugat cu success. Username: {new_user.username}, email: {new_user.email},'
                           f'first_name: {new_user.first_name}, last_name: {new_user.last_name}')

            History.objects.create(message=get_message, created_at=datetime.now(), active=True)

            #  # Trimitere de email fara template
            #
            #  subject = 'Added a new account '
            #  message = f'Congratulatiuons! Your username is {new_user.username}'
            # # send_mail() -> este o functie definita in cadrul framework - ului care faciliteaza trimiterea de email uri
            # # send_mail(subject, message,'office@office.ro', [new_user.email]) # pentru varianta de consola cand e setata in setting.py

            #  send_mail(subject, message,EMAIL_HOST_USER, [new_user.email])

            # Trimitere de email cu template

            details_user = {
                'fullname': f'{new_user.first_name} {new_user.last_name}',
                'username': f'{new_user.username}'
            }

            subject = 'Added a new account '
            message = get_template('mail.html').render(details_user)

            mail = EmailMessage(
                subject,
                message,
                EMAIL_HOST_USER,
                [new_user.email]
            )
            mail.content_subtype = 'html'
            mail.send()

        return redirect('login')
