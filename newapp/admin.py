from django.contrib import admin
from .models import Income, Outcome

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('tanggal', 'jumlah', 'sumber', 'deskripsi')

class OutcomeAdmin(admin.ModelAdmin):
    list_display = ('tanggal', 'jumlah', 'sumber', 'deskripsi')
        
admin.site.register(Income, IncomeAdmin)
admin.site.register(Outcome, OutcomeAdmin)
