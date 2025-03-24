from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import redirect, render
from django.views import View
from auth.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(csrf_exempt, name="dispatch")
class RegisterView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("TodoView")

        form = RegisterForm()
        return render(
            request,
            "auth/RegisterUser.html",
            context={"form": form},
        )

    def post(self, request):
        if request.user.is_authenticated:
            return redirect("TodoView")
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            if data["password"] != data["confirm_password"]:
                return redirect("RegisterView")

            data.pop("confirm_password")

            user = User.objects.create_user(**data)
            user.save()

        return redirect("RegisterView")


@method_decorator(csrf_exempt, name="dispatch")
class SignInView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("TodoView")

        form = LoginForm()
        return render(
            request,
            "auth/Login.html",
            context={"form": form},
        )

    def post(self, request):
        if request.user.is_authenticated:
            return redirect("TodoView")

        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            try:
                user = User.objects.get(email=data["email"]).username
                authenticated_user = authenticate(
                    username=user, password=data["password"]
                )
                login(request, authenticated_user)
            except Exception as e:
                print("Error de crendenciales")

        return redirect("SignInView")


class LogoutView(View):

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("SignInView")

        logout(request)
        return redirect("SignInView")
