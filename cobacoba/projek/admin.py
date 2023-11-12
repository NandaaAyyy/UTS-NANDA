from django.contrib import admin
from .models import Member, Profesi

# Register your models here.

class MemberAnggota():
  list_display = ("Nama", "NPM", "TANGGAL_LAHIR", "UNIVERSITAS",)
  
admin.site.register(Member)
admin.site.register(Profesi)