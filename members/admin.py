from django.contrib import admin
from .models import member

# Register your models here.

class memberAdmin(admin.ModelAdmin):
  list_display = ( 'firstname', 'lastname', 'joined_Date', 'phone', 'email')
  prepopulated_fields = {"slug": ("firstname", "lastname")}
  

admin.site.register(member, memberAdmin)
