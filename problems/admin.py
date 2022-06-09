from django.contrib import admin
from problems.models import Person, Pet
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    pass

class PetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person, PersonAdmin)
admin.site.register(Pet, PetAdmin)