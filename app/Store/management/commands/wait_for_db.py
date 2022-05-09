"""
Django command to wait for the db to be available.
"""

import time

from psycopg2 import OperationalError as Psycorpg20pError

