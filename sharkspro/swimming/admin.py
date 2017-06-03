from django.contrib import admin
from .models import Reviews
# Register your models here.

class ReviewsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['PostedName']}),
        ('PostedMobile', {'fields': ['PostedMobile'],'classes': ['collapse']}),
        ('PostedReview', {'fields': ['PostedReview'],'classes': ['collapse']}),
        ]
    list_display = ('PostedName','PostedMobile','PostedReview')

admin.site.register(Reviews, ReviewsAdmin)
