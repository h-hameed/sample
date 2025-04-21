from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Header, Line

class LineInline(admin.TabularInline):
    model = Line
    extra = 1

@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    inlines = [LineInline]