import exifread
from PIL import Image, ExifTags


def get_date_from_meta_info(image_path):
    """Извлекает дату съёмки разными способами"""
    # Способ 1: Используем Pillow (работает для большинства JPEG)
    try:
        img = Image.open(image_path)
        exif = img.getexif()
        if exif:
            for tag_id, value in exif.items():
                tag_name = ExifTags.TAGS.get(tag_id, tag_id)
                if tag_name in ['DateTimeOriginal', 'DateTimeDigitized']:
                    return value
    except (AttributeError, TypeError, KeyError, OSError):
        pass

    # Способ 2: Используем exifread для сложных случаев
    try:
        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f, details=False)
            for tag in ['EXIF DateTimeOriginal', 'EXIF DateTimeDigitized', 'Image DateTime']:
                if tag in tags:
                    return str(tags[tag])
    except Exception:
        pass

    return None