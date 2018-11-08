from __future__ import absolute_import #要写在第一行
import pymysql
from .celery import app as celery_app
pymysql.install_as_MySQLdb()

