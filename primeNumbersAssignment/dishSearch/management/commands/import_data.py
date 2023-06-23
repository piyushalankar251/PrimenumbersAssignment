import csv
import json
from django.core.management.base import BaseCommand
from dishSearch.models import Dish

class Command(BaseCommand):
    help = 'Load a dishes csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        if options['csv_file'] is not None:
            with open(options['csv_file'], 'rt') as f:
                reader = csv.reader(f, dialect='excel')
                next(reader)  # Skip the header row.
                for row in reader:
                    Dish.objects.create(
                        id=row[0],
                        name=row[1],
                        location=row[2],
                        items=json.loads(row[3]),
                        lat_long=row[4],
                        full_details=json.loads(row[5]),
                    )