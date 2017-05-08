from django.contrib import admin
from .models import *
# Register your models here.


class FlowerPreferenceInline(admin.TabularInline):
    model = FlowerPreference
    extra = 0


class CompositionColorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CompositionColor._meta.fields]

    class Meta:
        model = CompositionColor


class FlowerPreferenceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FlowerPreference._meta.fields]

    class Meta:
        model = FlowerPreference


class BoxSizeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BoxSize._meta.fields]

    class Meta:
        model = BoxSize


class BoxColorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BoxColor._meta.fields]

    class Meta:
        model = BoxColor


class IndividualCompositionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in IndividualComposition._meta.fields]
    inlines = [FlowerPreferenceInline]

    class Meta:
        model = IndividualComposition


admin.site.register(IndividualComposition, IndividualCompositionAdmin)
admin.site.register(BoxSize, BoxSizeAdmin)
admin.site.register(BoxColor, BoxColorAdmin)
admin.site.register(FlowerPreference, FlowerPreferenceAdmin)
admin.site.register(CompositionColor, CompositionColorAdmin)




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

