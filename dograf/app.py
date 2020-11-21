import psycopg2
import os
from time import sleep

import datetime as dt
from system import get_system_data



def get_conn():
    while True:
        try:
            conn = psycopg2.connect(
                dbname=os.environ["POSTGRES_DB"],
                user=os.environ["POSTGRES_USER"],
                password=os.environ["POSTGRES_PASSWORD"],
                host=os.environ["POSTGRES_HOST"]
            )
            return conn
        except psycopg2.errors.OperationalError:
            sleep(5)
        except Exception as e:
            raise

print("Container started!")
conn = get_conn()
HOSTNAME = open("/host/hostname", "r").readline().strip()

NAMESPACE = "system.monitor"
while True:
    with conn.cursor() as cur:
        cur.execute("INSERT INTO host_resources(namespace, hostname, data) VALUES (%s, %s, %s)", (NAMESPACE, HOSTNAME, get_system_data()))
        conn.commit()
    # function sleeps for 0.2s
    sleep(4.8)
conn.close()