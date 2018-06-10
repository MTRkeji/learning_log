from django.contrib import admin

# Register your models here.
from learning_logs.models import Topic,Entry,Software,Tip
admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Software)
admin.site.register(Tip)
