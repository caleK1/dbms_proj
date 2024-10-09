from django.contrib import admin
from .models import SchoolFastFacts
from .models import DistrictFastFacts
from .models import School
from .models import District
from .models import County

# Register your models here.
admin.site.register(SchoolFastFacts)
admin.site.register(DistrictFastFacts)
admin.site.register(School)
admin.site.register(District)
admin.site.register(County)