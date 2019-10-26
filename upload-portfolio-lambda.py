import json
import boto3
import StringIO
import zipfile
import mimetypes

PORTFOLIO_BUCKET='portfolio.bfraz.com'


def lambda_handler(event, context):
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:us-east-2:317605006010:deployPortfolioTopic')

    location = {
        "bucketName": 'portfoliobuild.bfraz.com',
        "objectKey": 'portfoliobuild.zip'
    }
    try:
        job = event.get("CodePipeline.job")

        if job:
            job_data = job["data"]["inputArtifacts"][0]
            location = job_data["location"]["s3Location"]

        s3 = boto3.resource('s3')

        portfolio_bucket = s3.Bucket(PORTFOLIO_BUCKET)
        build_bucket = s3.Bucket(location["bucketName"])

        portfolio_zip = StringIO.StringIO()
        build_bucket.download_fileobj(location["objectKey"], portfolio_zip)

        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj, nm, ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')

        topic.publish(Subject="portfolio build", Message="new version of site from build")
        if job:
            codepipeline = boto3.client('codepipeline')
            codepipeline.put_job_success_result(jobId=job["id"])
    except:
        topic.publish(Subject="portfolio build failed", Message="build failed")
        raise
    return {
        'statusCode': 200,
        'body': json.dumps('Job done!')
    }
