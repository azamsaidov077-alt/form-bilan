from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','description')
    search_fields = ('category_name',)
    list_filter = ('category_name',)
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','product_name','category_id','unit_price','discounted',)
    search_fields=('product_name',)
    list_filter=('product_name',)
admin.site.register(Products,ProductAdmin)
class SupplierAdmin(admin.ModelAdmin):
    list_display=('company_name','contact_name','address','city')
    search_fields=('company_name',)
    # list_filter=('company_name',)
admin.site.register(Suppliers,SupplierAdmin)
class OrderAdmin(admin.ModelAdmin):
    list_display=('customer_name','order_date','required_date','shipped_date')
    search_fields=('customer_name',)
    # list_filter=('customer_name',)
admin.site.register(Orders,OrderAdmin)