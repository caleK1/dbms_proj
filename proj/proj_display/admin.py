"""
    DBMS Project: Cale King, Eric Lynch, Jacob Seltzer
    Github Repo: https://github.com/caleK1/dbms_proj.git
"""

from django.contrib import admin
from .models import SchoolFastFacts
from .models import DistrictFastFacts
from .models import School
from .models import District
from .models import County
from .models import Demographic

# Register your models here.
admin.site.register(School)
admin.site.register(District)
admin.site.register(County)
admin.site.register(SchoolFastFacts)
admin.site.register(DistrictFastFacts)
admin.site.register(Demographic)
