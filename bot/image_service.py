import os
import secrets
from typing import List


class ImageService:
    """Contains methods that allow to interact with image library directory."""

    def __init__(self):
        """Caches outputs of some IO operations in order to limit unnecessary system calls."""
        self._image_dir_path = self._get_image_dir_path()
        self._available_categories = self._get_available_categories()

    @classmethod
    def _get_images_in_directory(cls, dir_path: str) -> List[str]:
        """Returns absolute paths of images found in the specified directory."""
        content = os.listdir(dir_path)
        return [
            os.path.join(dir_path, file) for file
            in content
            if os.path.isfile(os.path.join(dir_path, file))
            and os.path.splitext(file)[1] in ['.jpg', '.jpeg', '.png', '.gif', '.webp']
        ]

    @classmethod
    def _get_image_dir_path(cls):
        """Returns absolute path to the directory which contains image library."""
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        img_dir = os.path.join(cur_dir, "..", "images")
        return os.path.realpath(img_dir)

    @classmethod
    def _get_available_categories(cls) -> List[str]:
        """Lists names of available image categories.
        Image category is created when there is a subdirectory in the image library directory
        and this subdirectory contains at least one image."""
        img_dir = cls._get_image_dir_path()
        return [
            dir_name for dir_name
            in os.listdir(img_dir)
            if os.path.isdir(os.path.join(img_dir, dir_name))
            and len(cls._get_images_in_directory(os.path.join(img_dir, dir_name))) > 0
        ]

    def get_available_categories(self):
        """Returns cached list of available image categories."""
        return self._available_categories

    def get_random_image_in_category(self, category_name: str) -> str:
        """Returns absolute path to the random image from the specified category.
        If category does not exist, raises AttributeError."""
        if category_name not in self._available_categories:
            raise AttributeError("Invalid category: {}".format(category_name))
        category_dir = os.path.join(self._image_dir_path, category_name)
        images = self._get_images_in_directory(category_dir)
        return secrets.choice(images)
