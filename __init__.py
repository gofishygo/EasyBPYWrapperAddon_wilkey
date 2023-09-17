import os
import sys

ADDON_FOLDER_PATH = os.path.dirname(__file__)
VERSION = (0, 2, 0)
MODULE_NAME = "easybpy"
ADDON_NAME = (
    f"EasyBPY v{VERSION[0]}.{VERSION[1]}.{VERSION[2]}"
)

bl_info = {
    "name": "EasyBPY v0.2.0",
    "author": "Curtis Holt",
    "version": (0, 2, 0),
    "blender": (2, 83, 0),
    "description": "A module to simplify the use of the Blender Python API.",
    "category": "Development",
    "doc_url": "https://curtisholt.online/easybpy",
}


def register():
    print(f'ENABLED "{ADDON_NAME}" addon')

    print(f"\tadding {MODULE_NAME} to sys path: {ADDON_FOLDER_PATH}")
    sys.path.append(ADDON_FOLDER_PATH)


def unregister():
    print(f'DISABLE "{ADDON_NAME}" addon')

    print(f"\tremoving {MODULE_NAME} from sys path: {ADDON_FOLDER_PATH}")
    sys.path.remove(ADDON_FOLDER_PATH)


if __name__ == "__main__":
    register()
