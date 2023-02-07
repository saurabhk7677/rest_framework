from django.contrib import admin
from .models import TestCamp

# Register your models here.
@admin.register(TestCamp)
class TestCampAdmin(admin.ModelAdmin):
    list_display = ['title', 'mi', 'first', 'last', 'address1', 'address2', 'address3', 'city', 'state', 'postal_code', 'province',
    'country', 'date_of_birth', 'phone', 'dail_code', 'alt_phone', 'email', 'show', 'vender_id', 'rank', 'owner', 'comments']