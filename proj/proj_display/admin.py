"""
    DBMS Project: Cale King, Eric Lynch, Jacob Seltzer
    Github Repo: https://github.com/caleK1/dbms_proj.git
"""

from django.contrib import admin
from .models import School
from .models import District
from .models import County
from .models import SchoolInfo
from .models import GenderSchool
from .models import SchoolDemographic
from .models import ExtraDemoSchool

# Register your models here.
admin.site.register(School)
admin.site.register(District)
admin.site.register(County)
admin.site.register(SchoolInfo)
admin.site.register(GenderSchool)
admin.site.register(SchoolDemographic)
admin.site.register(ExtraDemoSchool)
