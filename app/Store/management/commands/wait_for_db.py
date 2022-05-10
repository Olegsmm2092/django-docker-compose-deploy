"""
Django command to wait for the db to be available.
"""

import time

from psycopg2 import OperationalError as Psycorpg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for db"""

    def handle(self, *args: None, **options: None):
        """Entrypoint for command."""
        self.stdout.write('Waiting for db ...')
        db_up = False
        while db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycorpg2OpError, OperationalError):
                self.stdout.write('db unavailable, not wait- 1 sec. ...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('db begin'))


        
                


        # return super().handle(*args, **options)
