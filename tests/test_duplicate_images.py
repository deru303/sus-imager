import os
import unittest
import difPy
from bot.image_service import ImageService


class DuplicateImagesTest(unittest.TestCase):
    """This test checks images folder and verifies if there are no duplicate images."""

    def setUp(self):
        self.image_service = ImageService()

    def test_look_for_duplicate_images(self):
        image_dir = self.image_service._get_image_dir_path()
        category_dirs = [
            os.path.join(image_dir, category_name)
            for category_name
            in self.image_service.get_available_categories()
        ]

        dif = difPy.build(category_dirs)
        search = difPy.search(dif)

        if len(search.result) == 0:
            return

        fail_msg = f"{len(search.result)} duplicates found:\n"
        for search_id, search_result in search.result.items():
            original_image = search_result["location"]
            duplicate_image = next(iter(search_result["matches"].values()))["location"]
            original_image_short = os.path.relpath(original_image, image_dir)
            duplicate_image_short = os.path.relpath(duplicate_image, image_dir)
            fail_msg += f"{original_image_short} appears to be duplicate of {duplicate_image_short}\n"

        fail_msg = fail_msg.rstrip()
        self.fail(fail_msg)


