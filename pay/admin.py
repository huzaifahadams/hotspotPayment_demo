from django.contrib import admin

from pay.models import packages, payment_num

# Register your models here.
admin.site.register(packages)
admin.site.register(payment_num)