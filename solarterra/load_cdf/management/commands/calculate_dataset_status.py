from django.core.management.base import BaseCommand
from django.apps import apps
import os
from load_cdf.models import *
from spacepy import pycdf


class Command(BaseCommand):

    def add_arguments(self, parser):

        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--update_all', action='store_true', help='Recalculate all datasets')
        group.add_argument('--dataset_tag', type=str, help='Recalculate specific dataset by tag')

    def handle(self, *args, **options):

        update_all = options['update_all']
        dataset_tag = options['dataset_tag']

        if update_all:
            #TODO: should also be written to logs
            print("Updating ALL datasets' file count and entry count")
            datasets = Dataset.objects.all()
            for dataset in datasets:
                dataset.dynamic.set_objects_count()
                dataset.dynamic.set_files_count()
            
        else:
            print(f"Updating file count and entry count for dataset with tag: {dataset_tag}")
            dataset = datasets = Dataset.objects.filter(tag = dataset_tag).first()
            dataset.dynamic.set_objects_count()
            dataset.dynamic.set_files_count()
            