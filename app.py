import io
import os
import time
from PIL import Image
from flask import Flask, request, jsonify
from celery import Celery
import oss2
from raven.contrib.flask import Sentry
from avatar_gen.letter_avatar import LetterAvatar
from avatar_gen.pixel_avatar import PixelAvatar
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


app = Flask(__name__)

# for docker deploy
# app.config.update(
    # CELERY_BROKER_URL=os.environ.get("DOCKER_REDIS_URL"),
    # CELERY_RESULT_BACKEND=os.environ.get("DOCKER_REDIS_URL"))

# for native os deploy
app.config.update(
CELERY_BROKER_URL=os.environ.get("NATIVE_REDIS_URL"),
CELERY_RESULT_BACKEND=os.environ.get("NATIVE_REDIS_URL"))

celery = make_celery(app)

# sentry settings
sentry = Sentry(app, dsn=os.environ.get("RAVEN_CONFIG_DSN"))

# aliyun oss key and secret
ALIYUN_ACCESS_KEY = os.environ.get('ALIYUN_ACCESS_KEY')
ALIYUN_ACCESS_SECRET = os.environ.get('ALIYUN_ACCESS_SECRET')
ALIYUN_OSS_BUCKET_NAME = os.environ.get('ALIYUN_OSS_BUCKET_NAME')
ALIYUN_OSS_ENDPOINT = os.environ.get('ALIYUN_OSS_ENDPOINT')
ALIYUN_OSS_PUBLIC_AVATAR_URL = os.environ.get('ALIYUN_OSS_PUBLIC_AVATAR_URL')


def save_avatar_to_oss(file_name, file_path):
    access_key = ALIYUN_ACCESS_KEY
    access_secret = ALIYUN_ACCESS_SECRET
    endpoint = ALIYUN_OSS_ENDPOINT
    bucket_name = ALIYUN_OSS_BUCKET_NAME
    auth = oss2.Auth(access_key, access_secret)
    bucket = oss2.Bucket(auth, endpoint, bucket_name)
    result = bucket.put_object_from_file(file_name, file_path)
    return result


@celery.task(name="generate_letter_avatar")
def generate_letter_avatar(size, string, filetype):
    now = time.time()
    image_byte_array = LetterAvatar.generate(size, string, filetype)
    file_name = 'avatar-gen-letter_avatar_' + str(now) + '.' + filetype.lower()
    file_path = "/tmp/" + file_name
    image = Image.open(io.BytesIO(image_byte_array))
    image.save(file_path)
    result = save_avatar_to_oss(file_name, file_path)
    status = result.status
    avatar_url = ALIYUN_OSS_PUBLIC_AVATAR_URL + '/' + file_name
    return status, avatar_url


@celery.task(name="generate_pixel_avatar")
def generate_pixel_avatar(size, string, filetype):
    now = time.time()
    pixel_avatar = PixelAvatar()
    image_byte_array = pixel_avatar.get_image(
        size=128, string=string, filetype='PNG')
    file_name = 'avatar-gen-pixel_avatar_' + str(now) + '.' + filetype.lower()
    file_path = "/tmp/" + file_name
    image = Image.open(io.BytesIO(image_byte_array))
    image.save(file_path)
    result = save_avatar_to_oss(file_name, file_path)
    status = result.status
    avatar_url = ALIYUN_OSS_PUBLIC_AVATAR_URL + '/' + file_name
    return status, avatar_url


@app.route('/api/v1/letter_avatar', methods=['GET'])
def letter_avatar():
    if request.method == 'GET':
        size = request.args.get('size', 256)
        string = request.args.get('string', 'avatar')
        filetype = request.args.get('filetype', 'PNG')
        celery_result = generate_letter_avatar.delay(int(size), string, filetype)
        result, avatar_url = celery_result.wait()
        if result == 200:
            resp = jsonify({'msg': '上传成功', 'avatar_url': avatar_url})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({'msg': '上传失败'})
            resp.status_code = 409
            return resp


@app.route('/api/v1/pixel_avatar', methods=['GET'])
def pixel_avatar():
    if request.method == 'GET':
        size = request.args.get('size', 256)
        string = request.args.get('string', 'avatar')
        filetype = request.args.get('filetype', 'PNG')
        celery_result = generate_pixel_avatar.delay(int(size), string, filetype)
        result, avatar_url = celery_result.wait()
        if result == 200:
            resp = jsonify({'msg': '上传成功', 'avatar_url': avatar_url})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({'msg': '上传失败'})
            resp.status_code = 409
            return resp


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)
