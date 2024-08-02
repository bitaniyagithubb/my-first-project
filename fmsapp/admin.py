from django.contrib import admin
from .models import Staff,Dam,Department,User,Sales
# Register your models here.
admin.site.register([Staff,Dam,Department,User])

@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ['name', 'category','slug', 'price', 'created']
    list_filter = ['category', 'created']
    list_editable = ['price', 'category']
    prepopulated_fields = {'slug': ('category',)}