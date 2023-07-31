from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import journal,Signature
# Register your models here.
#from import_export.admin import ImportExportModelAdmin


class RegisterJournal(admin.ModelAdmin):
    list_display = ['npp', 'dateInput', 'content','executor','datePeredachi','controlPeriod','painting','mark','nomenklatura']



class RegisterSignature(admin.ModelAdmin):
    list_display = ['numberInput', 'user', 'nomenklatura']

admin.site.register(journal,RegisterJournal)
admin.site.register(Signature,RegisterSignature)

