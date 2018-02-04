import io
from PIL import Image
from avatar_gen.letter_avatar import LetterAvatar


def main():
    image_byte_array = LetterAvatar.generate(size=128, string="lsdvincent@gmail.com", filetype="PNG")
    # image_byte_array = LetterAvatar.generate(128, "陈坚", "PNG")
    file_path = "/Users/Chen/PythonProjects/avatar-gen/letter_avatar.png"
    image = Image.open(io.BytesIO(image_byte_array))
    image.save(file_path)


if __name__ == '__main__':
    main()
