import boto3
import StringIO
import zipfile
import mimetypes

PORTFOLIO_BUCKET='portfolio.bfraz.com'
BUILD_BUCKET='portfoliobuild.bfraz.com'
PORTFOLIO_ZIP='portfoliobuild.zip'

s3 = boto3.resource('s3')

portfolio_bucket = s3.Bucket(PORTFOLIO_BUCKET)
build_bucket = s3.Bucket(BUILD_BUCKET)

portfolio_zip = StringIO.StringIO()
build_bucket.download_fileobj(PORTFOLIO_ZIP, portfolio_zip)

with zipfile.ZipFile(portfolio_zip) as myzip:
  for nm in myzip.namelist():
    obj = myzip.open(nm)
    portfolio_bucket.upload_fileobj(obj, nm, ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
    portfolio_bucket.Object(nm).Acl().put(ACL='public-read')


