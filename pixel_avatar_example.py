from avatar_gen.pixel_avatar import PixelAvatar


def main():
    # Example usage
    pixel_avatar = PixelAvatar(rows=10, columns=10)
    image_byte_array = pixel_avatar.get_image(
        string='lsdvincent@gmail.com', width=128, height=128, padding=10)

    return pixel_avatar.save(
        image_byte_array=image_byte_array, save_location='pixel_avatar.png')


if __name__ == '__main__':
    main()
