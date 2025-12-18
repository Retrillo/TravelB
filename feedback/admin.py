from django.contrib import admin

# Register your models here.
# feedback/admin.py
from django.contrib import admin
from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "category", "status", "created_at"]
    list_filter = ["status", "category", "created_at"]
    search_fields = ["name", "email", "subject", "message"]
    readonly_fields = ["created_at", "updated_at", "ip_address", "user_agent"]
    list_per_page = 20

    fieldsets = (
        (
            "Информация о пользователе",
            {"fields": ("name", "email", "phone", "ip_address", "user_agent")},
        ),
        ("Сообщение", {"fields": ("subject", "category", "message", "rating")}),
        ("Статус", {"fields": ("status", "created_at", "updated_at")}),
    )
