from django.contrib import admin
from pubg.models import pubg
class pubgset(admin.ModelAdmin):
    list_display=('school_name','school_place','about_school')


admin.site.register(pubg,pubgset)

# Register your models here.
