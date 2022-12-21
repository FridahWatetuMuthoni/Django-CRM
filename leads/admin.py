from django.contrib import admin
from .models import Lead, Agent, User, UserProfile, Category

# customizing the site header
admin.site.site_header = 'DJ-CRM DASHBOARD'
admin.site.site_title = 'DJ-CRM Administration'

# Register your models here.
admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)
admin.site.register(UserProfile)
admin.site.register(Category)
