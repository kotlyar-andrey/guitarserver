from django.contrib import admin
from django.db.models import JSONField
from django_json_widget.widgets import JSONEditorWidget
from .models import Payment, MobileUser


class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }


@admin.register(MobileUser)
class MobileUserAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'email', 'os')
    list_filter = ('os',)
    inlines = [PaymentInline]

