from django.contrib import admin

# Register your models here.
from .models import loan,loanoffers,Creditoffers,invest


admin.site.register(loan)
admin.site.register(loanoffers)
admin.site.register(Creditoffers)
admin.site.register(invest)