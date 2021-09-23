import psycopg2
import datetime
import time
import os
import config

PG_URL = config.PG_URL

def CreateTable(usrname):
    cur.execute("CREATE TABLE IF NOT EXISTS {} (year int, month int, start timestamp, finish timestamp, id serial primary key);".format(usrname))

def DropTable(usrname):
    cur.execute("DROP TABLE IF EXISTS {}".format(usrname))
    con.commit()

def Start(usrname):
    CreateTable(usrname)
    if isExistTable(usrname + '_tmp'):
        return False
    cur.execute("CREATE TABLE {}_tmp(start timestamp)".format(usrname))
    start = datetime.datetime.now()
    cur.execute("INSERT INTO {}_tmp(start) values (%s)".format(usrname), (start,))
    con.commit()
    return True