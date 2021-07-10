from django.contrib import admin
from .models import UserProfile, TopicTag
# Register your models here.


class AdminTopicTag(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-empty field-'

admin.site.register(TopicTag, AdminTopicTag)
admin.site.register(UserProfile)