from django.contrib import admin
from .models import Payment, MobileUser


class PaymentInline(admin.TabularInline):
    model = Payment


@admin.register(MobileUser)
class MobileUserAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'email', 'os')
    list_filter = ('os',)
    inlines = [PaymentInline]