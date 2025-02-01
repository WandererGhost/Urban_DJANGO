from django.contrib import admin
from .models import *


@admin.register(Buyer)
class AdminBuyer(admin.ModelAdmin):
    list_display = ('name', 'age', 'balance',)
    list_filter = ('balance', 'age')
    search_fields = ('name',)
    list_per_page = 30
    readonly_fields = ('balance',)


@admin.register(Game)
class AdminGame(admin.ModelAdmin):
    list_display = ('title', 'size', 'cost',)
    list_filter = ('size', 'cost',)
    search_fields = ('title',)
    list_per_page = 20


@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display = ('title', 'date',)
    list_filter = ('date',)
    search_fields = ('title', 'date')
    list_per_page = 10
