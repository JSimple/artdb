from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from time import time
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

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    return "This is the index route. It returns this placeholder string."

@app.route('/get_time', methods=["GET"])
def get_current_time():
    return {'time': time()}

@app.route('/files', methods=["GET"])
def get_files():
    s3_resource = resource('s3')
    bucket = s3_resource.Bucket(s3_bucket)
    summaries = bucket.objects.all()
    
    return render_template('files.html', bucket=bucket,files=summaries)

if __name__=='__main__':
    app.run(debug=True)