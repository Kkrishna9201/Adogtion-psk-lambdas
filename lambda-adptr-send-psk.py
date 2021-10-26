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

item_count=0;

def lambda_handler(event, context):
    """
    This function fetches content from MySQL RDS instance
    """
    with conn.cursor() as cur:
    
        cur.execute('insert into adopter (Dog_Id,First_Name,Last_Name,Mobile_No,EmailID,Location,Donation_Amount) values(%s, %s, %s, %s, %s, %s, %s)',(event['dogid'], event['fname'], event['lname'], event['mobile'], event['email'], event['location'], event['amount']))
        conn.commit()
        
        cur.execute("select Organization_Name, Location, Email, Contact from organization where organization.Dog_ID = %s", event['dogid'])
        details = []
        for row in cur:
            details.append(row)
        conn.commit()
        
        cur.execute("delete from organization where organization.Dog_ID = %s",event['dogid'])
        conn.commit()
    
    ses = boto3.client('ses')
    
    body = """ Thank You for this adoption!
    
    
    		Summary of your booking:
    		
    		DogID : %s,
    		First Name : %s,
    		Last Name : %s,
    		Mobile No. : %s,
    		Email Id : %s,
    		Location : %s,
    		Donation Amount : %s
    		
    		
    		Organization Contact Details : 
    		
    		Organization_Name : %s,
    		Location : %s,
    		Email : %s,
    		Contact : %s
    		
    """ % (event['dogid'], event['fname'], event['lname'], event['mobile'], event['email'], event['location'], event['amount'], details[0][0], details[0][1], details[0][2], details[0][3])

    ses.send_email(
	    Source = 'shubhambhonkhade237@gmail.com',
	    Destination = {
		    'ToAddresses': [
			    event['email']
		    ]
	    },
	    Message = {
		    'Subject': {
			    'Data': 'Booking is Confirmed',
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
    
    
    body = """ Congratulations!!! Dog from your organization has been booked.
    
          	
          	
            Here are the adopter details:
    		
    		First Name : %s,
    		Last Name : %s,
    		DogID : %s,
    		Mobile No. : %s,
    		Email Id : %s,
    		Location : %s,
    		Donation Amount : %s
    """ % (event['fname'], event['lname'], event['dogid'], event['mobile'], event['email'], event['location'], event['amount'])

    ses.send_email(
	    Source = 'shubhambhonkhade237@gmail.com',
	    Destination = {
		    'ToAddresses': [
			    details[0][2]
		    ]
	    },
	    Message = {
		    'Subject': {
			    'Data': 'Congratulations!!! Dog from your organization has been booked',
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
    
    
    return "Adopter details stored successfully and sent confirmation email"
