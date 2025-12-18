from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import DetailView, UpdateView  # Добавьте UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def news_home(request):
    news = Article.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.name = request.user.username
            article.save()
            return redirect('news_home')
    else:
        form = ArticleForm(initial={'date': timezone.now()})
    return render(request, 'news/create.html', {'form': form})



@login_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.user.username != article.name:
        return redirect('news_home')
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('news_home')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'news/create.html', {'form': form, 'edit': True})


class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'news/create.html'

    def test_func(self):
        article = self.get_object()
        return self.request.user.username == article.name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context