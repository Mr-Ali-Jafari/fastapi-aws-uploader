from app.utils import cloud,rappidmq
from fastapi import FastAPI, UploadFile, File
from starlette.responses import FileResponse 

# aws configuration
aws_access_key = 'YOUR_AWS_ACCESS_KEY'
aws_secret_key = 'YOUR_AWS_SECRET_KEY'
bucket_name = 'YOUR_BUCKET_NAME'



app = FastAPI()


# Upload file to S3
@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    file_content = await file.read()
    await cloud.upload_file_to_s3(file_content, file.filename, aws_access_key, aws_secret_key, bucket_name)
    await rappidmq.rappid_mq(file.filename,file_content)
    return {"message": "File uploaded successfully"}


@app.get("/")
async def main():
    content = 'templates/index.html'
    return FileResponse(content)