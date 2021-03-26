from django.contrib import admin
from .models import SampleModel,BlogModel,AnimeModel,RamennModel

admin.site.register(SampleModel)
admin.site.register(BlogModel)
admin.site.register(AnimeModel)
admin.site.register(RamennModel)