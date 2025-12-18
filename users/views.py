from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


def register(request):
    """Регистрация нового пользователя"""
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Создаем пользователя
            messages.success(request, "Аккаунт успешно создан!")
            return redirect("login")
        else:
            messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
    else:
        form = UserRegisterForm()  # GET запрос - пустая форма
    return render(request, "users/register.html", {"form": form})


def login_view(request):
    """Авторизация пользователя"""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Получаем объект пользователя
            login(request, user)  # Логиним пользователя в сессию
            return redirect("profile")  # Перенаправляем в профиль
        else:
            messages.error(request, "Неверный логин или пароль")
    else:
        form = AuthenticationForm()  # GET запрос - пустая форма
    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    """Выход из системы"""
    logout(request)  # Разлогиниваем пользователя
    return redirect("login")


@login_required  # Только для авторизованных
def profile_view(request):
    """Просмотр профиля пользователя"""
    return render(request, "users/profile.html", {"user": request.user})


@login_required
def profile_edit(request):
    """Редактирование профиля и смена пароля"""
    if request.method == "POST":
        # Инициализируем формы с данными из запроса
        user_form = UserUpdateForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)

        # Если обе формы валидны - сохраняем всё
        if user_form.is_valid() and password_form.is_valid():
            user_form.save()  # Сохраняем данные пользователя
            password_form.save()  # Сохраняем новый пароль
            update_session_auth_hash(request, password_form.user)  # Обновляем сессию
            messages.success(request, "✅ Профиль успешно обновлён!")
            return redirect("profile")

        # Если только данные пользователя валидны
        elif user_form.is_valid():
            user_form.save()
            messages.success(request, "✅ Данные профиля обновлены!")
            return redirect("profile")

        # Если только пароль валиден
        elif password_form.is_valid():
            password_form.save()
            update_session_auth_hash(
                request, password_form.user
            )  # Важно для сохранения авторизации
            messages.success(request, "🔒 Пароль успешно изменён!")
            return redirect("profile")

    else:
        # GET запрос - заполняем формы текущими данными
        user_form = UserUpdateForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)

    return render(
        request,
        "users/profile_edit.html",
        {"user_form": user_form, "password_form": password_form},
    )
