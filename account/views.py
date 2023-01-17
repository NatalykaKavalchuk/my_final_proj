from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy

from django.contrib.auth import login, authenticate

from account.forms import LoginForm, UserRegisterForm


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Profile.objects.create(username=user)
            messages.info(request, "Thanks for registering. You are now logged in.")

            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserRegisterForm()
    return render(request=request, template_name="registration/register.html", context={'form': form})


# class CustomLoginView(LoginView):
#     form_class = LoginForm
#
#     def form_valid(self, form):
#         remember_me = form.cleaned_data.get('remember_me')
#
#         if not remember_me:
#             self.request.session.set_expiry(0)
#             self.request.session.modified = True
#         return super(CustomLoginView, self).form_valid(form)
#
#     render(request, 'users/login.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.info(request, 'Неверно имя пользователя или пароль')
    return render(request, 'registration/login.html')

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'registration/password_reset.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'registration/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')
