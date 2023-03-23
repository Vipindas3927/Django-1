from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(student)
admin.site.register(employee)
admin.site.register(employee2)
admin.site.register(fileUpload)
admin.site.register(uploadModel)
admin.site.register(itemBillModel)

