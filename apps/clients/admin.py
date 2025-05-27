from django.contrib import admin
from apps.clients.models.models import Client, LegalDetails, IndividualDetails

# Inline для юридических деталей
class LegalDetailsInline(admin.StackedInline):
    model = LegalDetails
    can_delete = False
    verbose_name_plural = "Юридическая информация"

# Inline для физических деталей
class IndividualDetailsInline(admin.StackedInline):
    model = IndividualDetails
    can_delete = False
    verbose_name_plural = "Физическая информация"

# Основная админка клиента
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'phone', 'is_legal', 'created_at')
    search_fields = ('name', 'surname', 'email', 'phone')
    list_filter = ('is_legal', 'created_at')

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        if obj.is_legal:
            return [LegalDetailsInline(self.model, self.admin_site)]
        else:
            return [IndividualDetailsInline(self.model, self.admin_site)]

# Можно также зарегистрировать напрямую, если хочешь видеть их отдельно
@admin.register(LegalDetails)
class LegalDetailsAdmin(admin.ModelAdmin):
    list_display = ('client', 'inn', 'kpp', 'ogrn')

@admin.register(IndividualDetails)
class IndividualDetailsAdmin(admin.ModelAdmin):
    list_display = ('client', 'unp', 'passport_number', 'birth_date')
