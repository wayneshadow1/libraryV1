from django.contrib import admin

# Register your models here.
from .models import asset ,asset_grouping,asset_type,Project
admin.site.register(asset)
admin.site.register(asset_grouping)
admin.site.register(asset_type)

class AssetInline(admin.TabularInline):
      model = asset


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
      inlines = [AssetInline]
