# avatar-gen

[![Build Status](https://travis-ci.org/lsdlab/avatar-gen.svg?branch=master)](https://travis-ci.org/lsdlab/avatar-gen)

pillow 头像生成，中文或英文首字母或者随机像素化。

Using pillow for generate avatars, first letter of string in Chinese and English or random pixle like avatars.

参考了 https://github.com/maethor/avatar-generator 和 https://github.com/richardasaurus/randomavatar

第一个库用的字体不能生成中文，换成了思源黑体，然后位置也调整了一下才能把字放在中间。


## Flask API

参考 `app.py`，用了 celery，再 Docker 化做成微服务。

``` shell
python app.py    # python 单进程
gunicorn app:app -c gunicorn.conf    # four worker and gevent
celery -A app.celery worker --loglevel=info --autoscale=4,2     # celery job queue
```

## Docker 运行

用 Docker 运行请注意 `app.py` 里面的 `app.config.update()` Redis 作为 Celery 的 Broker,
redis host 用字符串 `redis`。

``` shell
docker-compose up
```

两个 API，都是 `GET` 方法，`filetype` 参数可以不传：

``` shell
curl -X GET 'http://localhost:5000/api/v1/letter_avatar?size=128&string=lsdvincent@gmail.com&filetype=PNG'
curl -X GET 'http://localhost:5000/api/v1/pixel_avatar?size=128&string=lsdvincent@gmail.com&filetype=PNG'
```


## Python 项目包安装方法 Python project package Installation:

``` shell
pip install git+https://github.com/lsdlab/avatar-gen.git
```


## 使用方法 Usage:

生成出来的是 image byte array，自己用 PIL 保存。

generate result is image byte array, you need to save to file using PIL.

``` python
import io
from PIL import Image
from avatar_gen.letter_avatar import LetterAvatar
from avatar_gen.pixel_avatar import PixelAvatar

# generate letter avatar in Chinese or Enginlish character
image_byte_array = LetterAvatar.generate(size=128, string="lsdvincent@gmail.com", filetype="PNG")
# image_byte_array = LetterAvatar.generate(size=128, string="lsdvincent@gmail.com", filetype="PNG")
file_path = "/Users/Chen/PythonProjects/avatar-gen/letter_avatar.png"
image = Image.open(io.BytesIO(image_byte_array))
image.save(file_path)

# generate pixel avatar
pixel_avatar = PixelAvatar(rows=10, columns=10)
image_byte_array = pixel_avatar.get_image(size=128, string="lsdvincent@gmail.com", filetype="PNG")
file_path = "/Users/Chen/PythonProjects/avatar-gen/pixel_avatar.png"
image = Image.open(io.BytesIO(image_byte_array))
image.save(file_path)
# or you can save image file using instance function
# return pixel_avatar.save(
    # image_byte_array=image_byte_array, save_location='pixel_avatar.png')
```


## 生成示例 examples:

![](http://breakwire.oss-cn-shanghai.aliyuncs.com/letter_avatar.png)
![](http://breakwire.oss-cn-shanghai.aliyuncs.com/letter_avatar_1.png)
![](http://breakwire.oss-cn-shanghai.aliyuncs.com/pixel_avatar.png)

