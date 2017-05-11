from django.contrib import admin
from .models import *
# Register your models here.


class IndividualCompositionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in IndividualComposition._meta.fields]

    class Meta:
        model = IndividualComposition


admin.site.register(IndividualComposition, IndividualCompositionAdmin)

# class IndividualCompositionAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Order._meta.fields]
#     inlines = [ProductInOrderInline]
#     class Meta:
#         model = Order
#
# admin.site.register(Order, OrderAdmin)
#
# class ProductInOrderAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in ProductInOrder._meta.fields]
#     class Meta:
#         model = ProductInOrder
#
# admin.site.register(ProductInOrder, ProductInOrderAdmin)

