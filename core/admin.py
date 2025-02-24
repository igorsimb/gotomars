from django.contrib import admin

from core.models import Feature


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)


admin.site.register(Feature, FeatureAdmin)
