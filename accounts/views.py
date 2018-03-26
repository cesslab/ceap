from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import LoginForm


class LoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'accounts/login.html'

    def get_form_kwargs(self):
        kwargs = super(LoginView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        return redirect(reverse_lazy('experiments:home'))

# def login_page(request):
#     form = LoginForm(request.POST)
#     context = {'form': form}
#     if form.is_valid():
#         email = form.cleaned_data.get("email")
#         password = form.cleaned_data.get("password")
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('/login')
#         else:
#             print("Error")
#
#     return render(request, "accounts/login.html", context)
