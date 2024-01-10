import os
import unittest

from bot.image_service import ImageService


class InvalidImagesTest(unittest.TestCase):
    """This test checks images folder and verifies if there are no files with unknown extension."""

    def setUp(self):
        self.image_service = ImageService()

    def test_for_invalid_images(self):
        valid_extensions = self.image_service._get_allowed_img_extensions()
        image_dir = self.image_service._get_image_dir_path()
        category_dirs = [
            os.path.join(image_dir, category_name)
            for category_name
            in self.image_service.get_available_categories()
        ]

        failed = False
        failed_msg = "Image files have unrecognized extensions:\n"
        for category_dir in category_dirs:
            for filename in os.listdir(category_dir):
                if not any([filename.lower().endswith(ext.lower()) for ext in valid_extensions]):
                    filepath = os.path.join(category_dir, filename)
                    filepath_short = os.path.relpath(filepath, image_dir)
                    failed = True
                    failed_msg += filepath_short + "\n"

        if failed:
            failed_msg = failed_msg.rstrip()
            self.fail(failed_msg)