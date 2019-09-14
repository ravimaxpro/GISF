from django.contrib import admin
from myapp.models import employees1,departments1,Student,Product,Product1
# Register your models here.
#class ProductAdmin(admin.ModelAdmin):
#    list_display=["title","price"]

admin.site.register(employees1,)
admin.site.register(departments1)
admin.site.register(Student)
admin.site.register(Product)
admin.site.register(Product1)