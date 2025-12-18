from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import FeedbackForm
from .models import Feedback
import logging

logger = logging.getLogger(__name__)


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():

            feedback = form.save(commit=False)


            feedback.ip_address = request.META.get('REMOTE_ADDR')
            feedback.user_agent = request.META.get('HTTP_USER_AGENT', '')

            feedback.save()


            logger.info(f'Новое обращение от {feedback.name} ({feedback.email})')


            try:
                send_mail(
                    f'Новое обращение: {feedback.subject}',
                    f'От: {feedback.name}\nEmail: {feedback.email}\n\n{feedback.message}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=True,
                )
            except Exception as e:
                logger.error(f'Ошибка отправки email: {e}')


            messages.success(request, 'Ваше сообщение успешно отправлено! Мы свяжемся с вами в ближайшее время.')


            return redirect('feedback_success')
    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback.html', {'form': form})


def feedback_success(request):
    return render(request, 'feedback/success.html')