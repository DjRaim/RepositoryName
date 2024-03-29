from django.conf import settings
from django.contrib.auth import get_user_model, login, views as auth_views
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils.http import base36_to_int, int_to_base36
from django.utils.translation import ugettext_lazy as _
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from user.forms import UserCreationForm


def home(request):
    return render(request, 'profile/home.html')



def logout(request):
    request.session.flush()
    return redirect('/user/')


class LoginView(auth_views.LoginView):
    template_name = 'profile/login.html'

# class LogoutView(auth_views.LogoutView):
#     template_name = 'user/logout.html'


class SignupView(CreateView):
    template_name = 'user/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('user:signup-done')

    def form_valid(self, form):
        ret = super().form_valid(form)

        site_name = 'Local Forum'
        domain = 'localhost'

        uid = int_to_base36(self.object.id)
        token = default_token_generator.make_token(self.object)
        mail_context = {
            'email': self.object.email,
            'domain': domain,
            'site_name': site_name,
            'uid': uid,
            'user': self.object,
            'token': token,
            'url': self.request.build_absolute_uri(reverse(
                'user:signup-confirm',
                kwargs={'uidb36': uid, 'token': token}
            ))
        }

        send_mail(
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.object.email],
            message='',
            subject=_('Спасибо, ваша регистрация прошла успешно!'),
            html_message=render_to_string(template_name='user/email/signup.html', context=mail_context),
        )

        return ret


class SignupDoneView(TemplateView):
    template_name = 'user/signup-done.html'


class SignUpConfirmView(View):
    def get(self, request, *args, **kwargs):

        uidb36 = kwargs.get('uidb36')
        token = kwargs.get('token')

        try:
            uid_int = base36_to_int(uidb36)
        except ValueError:
            raise Http404

        user = get_object_or_404(get_user_model(), id=uid_int)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()

        login(request, user=user)
        return redirect('forum:home')


"""
1 Создание страницы (въюха + урл)
2 Создание шаблона, привязка к въюхе
3 Создание формы
4 Привязка формы к въюхе
5 Получение данных с формы
6 Валидация данных
7 Сохранение в базу
8 Отправка письма
9 Получение данных с письма
10 Проверка данных с письма
11 Активация пользователя
"""
