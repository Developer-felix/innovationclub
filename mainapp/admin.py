from django.contrib import admin
from .models import Community,Leader,Project, Feedback, Community_Event

admin.site.register(Community)
admin.site.register(Leader)
admin.site.register(Project)
admin.site.register(Feedback)
admin.site.register(Community_Event)
