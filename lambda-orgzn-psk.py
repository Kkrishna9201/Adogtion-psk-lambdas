import json
import sys
import logging
import pymysql
import hashlib
import boto3

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
  
    item_count = 0
    
    with conn.cursor() as cur:
      
        cur.execute('insert into organization (Organization_Name,Location,Email,Contact,Breed,Image) values(%s, %s, %s, %s, %s, %s)',(event['orgzn_name'], event['location'], event['email'], event['contact'], event['breed'], event['image']))
        conn.commit()
        cur.execute("select * from organization")
        for row in cur:
            item_count += 1
            logger.info(row)
            print(row)
    conn.commit()
    
    ses = boto3.client('ses')
    
    body = """ Thank You for this initiative!
    
    
    		Summary of details submitted by you:
    		
    		Organization Name : %s,
    		Location : %s,
    		Email ID : %s,
    		Mobile No. : %s,
    		Dog Breed : %s
    		
    """ % (event['orgzn_name'], event['location'], event['email'], event['contact'], event['breed'])

    ses.send_email(
	    Source = 'shubhambhonkhade237@gmail.com',
	    Destination = {
		    'ToAddresses': [
			    event['email']
		    ]
	    },
	    Message = {
		    'Subject': {
			    'Data': 'Dog Details Submitted',
			    'Charset': 'UTF-8'
		    },
		    'Body': {
			    'Text':{
				    'Data': body,
				    'Charset': 'UTF-8'
			    }
		    }
	    }
    )
    
    
    return "Added %d items from RDS MySQL table" %(item_count)
    
 
