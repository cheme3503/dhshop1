from django.contrib import admin
import csv
import datetime
from django.http import HttpResponse
from .models import OrderItem, Order
# Register your models here.

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
    writer=csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])

    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime("%Y-%m-%d")
            data_row.append(value)
        writer.writerow(data_row)

    return response
export_to_csv.short_description ='Export to CSV'

from django.urls import reverse
from django.utils.safestring import mark_safe

def order_detail(obj):
    return mark_safe('<a href="{}">Detail</a>'.format(reverse('order:admin_order_detail', args=[obj.id])))

order_detail.short_description = 'Detail'

def order_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(reverse('order:admin_order_pdf', args=[obj.id])))

order_pdf.short_description = 'PDF'

# def order_pdf(obj):
#     return mark_safe('<a href="{}">PDF</a>'.format(reverse('order:admin_order_pdf', args=[obj.id])))
#
# order_pdf.short_description = 'PDF'

from .models import OrderItem, Order
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']




@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','address','postal_code','city','paid',order_detail,order_pdf,'created','updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [export_to_csv]



