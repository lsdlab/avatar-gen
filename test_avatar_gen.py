import os
import io
from PIL import Image
from avatar_gen.letter_avatar import LetterAvatar
from avatar_gen.pixel_avatar import PixelAvatar


def generate_letter_avatar():
    image_byte_array = LetterAvatar.generate(
        size=128, string="lsdvincent@gmail.com", filetype="PNG")
    file_path = "/tmp/letter_avatar.png"
    image = Image.open(io.BytesIO(image_byte_array))
    image.save(file_path)
    return file_path


def geneate_pixel_avatar():
    pixel_avatar = PixelAvatar(rows=10, columns=10)
    image_byte_array = pixel_avatar.get_image(
        size=128, string='lsdvincent@gmail.com', filetype="PNG")
    file_path = "/tmp/pixel_avatar.png"
    image = Image.open(io.BytesIO(image_byte_array))
    image.save(file_path)
    return file_path


def test_letter_avatar():
    assert os.path.exists(generate_letter_avatar()) == True


def test_pixel_avatar():
    assert os.path.exists(geneate_pixel_avatar()) == True
