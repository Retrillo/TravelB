from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def news_home(request):
    """Главная страница со списком всех новостей"""
    news = Article.objects.order_by("-date")  # Сортируем по дате (сначала новые)
    return render(request, "news/news_home.html", {"news": news})


# Только авторизованные могут создавать статьи
@login_required
def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)  # Создаем объект, но не сохраняем в БД
            article.name = request.user.username  # Указываем автора
            article.save()  # Теперь сохраняем
            return redirect("news_home")
    else:
        # Форма с текущей датой по умолчанию
        form = ArticleForm(initial={"date": timezone.now()})
    return render(request, "news/create.html", {"form": form})


# Просмотр детальной информации о статье
class NewsDetailView(DetailView):
    model = Article  # Модель для работы
    template_name = "news/details_view.html"  # Шаблон
    context_object_name = "article"  # Имя переменной в шаблоне


# Редактирование статьи
class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "news/create.html"

    def test_func(self):
        """Проверка прав на редактирование"""
        article = self.get_object()  # Получаем текущую статью
        return (
            self.request.user.username == article.name
        )  # Только автор может редактировать

    def get_context_data(self, **kwargs):
        """Добавляем флаг редактирования в контекст"""
        context = super().get_context_data(**kwargs)
        context["edit"] = True  # Передаем в шаблон, что это редактирование
        return context
