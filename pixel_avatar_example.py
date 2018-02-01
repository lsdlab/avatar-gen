import io
from PIL import Image
from avatar_gen.pixel_avatar import PixelAvatar


def main():
    pixel_avatar = PixelAvatar(rows=10, columns=10)
    image_byte_array = pixel_avatar.get_image(
        string='lsdvincent@gmail.com', width=108, height=108, padding=10)
    file_path = "/Users/Chen/PythonProjects/avatar-gen/pixel_avatar.png"
    image = Image.open(io.BytesIO(image_byte_array))
    image.save(file_path)
    # return pixel_avatar.save(
        # image_byte_array=image_byte_array, save_location='pixel_avatar.png')


if __name__ == '__main__':
    main()
