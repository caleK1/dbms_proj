from proj_display.models import District
from django.core.management.base import BaseCommand


class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		districts_to_delete = District.objects.exclude(district_name__icontains='SD')
		districts_to_delete.delete()
		print(f"Deleted {districts_to_delete.count()} districts.")
