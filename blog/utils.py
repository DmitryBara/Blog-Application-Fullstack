import os, json, boto3
from django.http import JsonResponse


# for AWS S3 sign. request.method == 'POST'
def sign_s3(request):
    S3_BUCKET = os.environ.get('S3_BUCKET')

    file_name = request.session['a_uid']
    file_type = request.GET.get('file_type')
    s3 = boto3.client('s3')

    presigned_post = s3.generate_presigned_post(
        Bucket=S3_BUCKET,
        Key=file_name,
        Fields={"acl": "public-read", "Content-Type": file_type},
        Conditions=[
            {"acl": "public-read"},
            {"Content-Type": file_type}
        ],
        ExpiresIn=3600
    )

    json_object = {
        'data': presigned_post,
        'url': 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, file_name)
    }

    return JsonResponse(json_object)
