from django.contrib import admin
from .models import SchoolFastFacts
from .models import DistrictFastFacts

# Register your models here.
admin.site.register(SchoolFastFacts)
admin.site.register(DistrictFastFacts)