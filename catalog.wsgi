#!/usr/bin/python
import sys
sys.stdout = sys.stderr

sys.path.insert(0,"/var/www/catalog")

from project import app as application

