from django.contrib import admin
from .models import SchoolFastFacts
from .models import DistrictFastFacts
from .models import DistrictFiscalData


# Register your models here.
admin.site.register(SchoolFastFacts)
admin.site.register(DistrictFastFacts)
admin.site.register(DistrictFiscalData)
