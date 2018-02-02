# avatar-gen

[![Build Status](https://travis-ci.org/lsdlab/avatar-gen.svg?branch=master)](https://travis-ci.org/lsdlab/avatar-gen)

pillow 头像生成，中英文首字母或者随机像素化。

Using pillow for generate avatars, first letter of string in Chinese and English or random pixle like avatars.

参考了 https://github.com/maethor/avatar-generator 和 https://github.com/richardasaurus/randomavatar

第一个库用的字体不能生成中文，换成了思源黑体，然后位置也调整了一下才能把字放在中间。


## 安装方法 Installation:

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
image_byte_array = LetterAvatar.generate(128, "lsdvincent@gmail.com", "PNG")
# image_byte_array = LetterAvatar.generate(128, "陈坚", "PNG")
file_path = "/Users/Chen/PythonProjects/avatar-gen/letter_avatar.png"
image = Image.open(io.BytesIO(image_byte_array))
image.save(file_path)

# generate pixel avatar
pixel_avatar = PixelAvatar(rows=10, columns=10)
image_byte_array = pixel_avatar.get_image(
    string='lsdvincent@gmail.com', width=108, height=108, padding=10)
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
