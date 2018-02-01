
"""
    Generates default avatars from a given string (such as username).

    Usage:

    >>> from avatar_generator import Avatar
    >>> photo = Avatar.generate(128, "example@sysnove.fr", "PNG")
"""

import io
from PIL import Image
from avatar_gen.letter_avatar import LetterAvatar


def main():
    file_path = "/Users/Chen/PythonProjects/avatar-gen/letter_avatar.png"
    # image_byte_array = LetterAvatar.generate(128, "lsdvincent@gmail.com", "PNG")
    image_byte_array = LetterAvatar.generate(128, "陈坚", "PNG")
    image = Image.open(io.BytesIO(image_byte_array))
    image.save(file_path)


if __name__ == '__main__':
    main()
