import json
import sys
import logging
import pymysql
import hashlib
#import jwt
from datetime import date
#rds settings
rds_host  = "psk-rds.csaruqlxxway.us-east-1.rds.amazonaws.com"
name = "admin"
password = "master123"
db_name = "psk_db"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
def lambda_handler(event, context):
   
   
  
    order_data = []
  
    with conn.cursor() as cur:
        sql = "SELECT * FROM `organization`"
        cur.execute(sql)
        for row in cur:
            order_data.append(row)
    conn.commit()

  

    return{
        "order_data": order_data,
      
    }
    import json
import sys
import logging
import pymysql
import hashlib
#import jwt
from datetime import date
#rds settings
rds_host  = "psk-rds.csaruqlxxway.us-east-1.rds.amazonaws.com"
name = "admin"
password = "master123"
db_name = "psk_db"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
def lambda_handler(event, context):
   
   
  
    order_data = []
  
    with conn.cursor() as cur:
        sql = "SELECT * FROM `organization`"
        cur.execute(sql)
        for row in cur:
            order_data.append(row)
    conn.commit()

  

    return{
        "order_data": order_data,
      
    }
    import json
import sys
import logging
import pymysql
import hashlib
#import jwt
from datetime import date
#rds settings
rds_host  = "psk-rds.csaruqlxxway.us-east-1.rds.amazonaws.com"
name = "admin"
password = "master123"
db_name = "psk_db"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
def lambda_handler(event, context):
   
   
  
    order_data = []
  
    with conn.cursor() as cur:
        sql = "SELECT * FROM `organization`"
        cur.execute(sql)
        for row in cur:
            order_data.append(row)
    conn.commit()

  

    return{
        "order_data": order_data,
      
    }
    
