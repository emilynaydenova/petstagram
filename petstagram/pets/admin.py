from django.contrib import admin

# Register your models here.
from pets.models import Pet, Like

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'age','likes_count']
    list_filter = ['type']

    def likes_count(self,obj):
        return obj.like_set.count()


# admin.site.register(Pet, PetAdmin)
admin.site.register(Like)
