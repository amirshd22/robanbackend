from django.contrib import admin
from .models import UserProfile, TopicTag,Member
# Register your models here.


class AdminTopicTag(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-empty field-'

admin.site.register(TopicTag, AdminTopicTag)
admin.site.register(UserProfile)
admin.site.register(Member)
