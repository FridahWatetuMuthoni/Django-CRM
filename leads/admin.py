from django.contrib import admin
from .models import Lead, Agent, User

# Register your models here.
admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)
