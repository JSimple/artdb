from flask import render_template
from flask import Blueprint
from boto3 import resource, client
from dotenv import dotenv_values

config = dotenv_values(".flaskenv")
aws_key_id = config["AWS_KEY"]
aws_secret_access_key = config["AWS_SECRET_ACCESS_KEY"]
s3_bucket = config["S3_Bucket"]

s3 = client(
    's3',
    aws_access_key_id= aws_key_id,
    aws_secret_access_key= aws_secret_access_key
)

files_api = Blueprint('files_api', __name__, template_folder='../templates')

@files_api.route('/files', methods=["GET"])
def get_files():
    s3_resource = resource('s3')
    bucket = s3_resource.Bucket(s3_bucket)
    summaries = bucket.objects.all()
    
    return render_template('files.html', bucket=bucket,files=summaries)