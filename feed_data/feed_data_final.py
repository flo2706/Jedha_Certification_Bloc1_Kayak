import os
from dotenv import load_dotenv
import boto3

print("Current working directory:", os.getcwd())
print("Listing current directory:", os.listdir())
load_dotenv()

session = boto3.Session(aws_access_key_id=os.environ["AWS_KEY"], 
                        aws_secret_access_key=os.environ["AWS_SECRET_KEY"])

s3 = session.resource("s3")

bucket = s3.Bucket("flodussartprojectkayak")

file_name = "project_Kayak/create_final_csv/hotels_weather_final.csv"

bucket.upload_file(file_name, "projectKayack/src/final_ter.csv")