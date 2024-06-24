import os
import sys

ADDON_FOLDER_PATH = os.path.dirname(__file__)
VERSION = (0, 2, 0)
MODULE_NAME = "IRE_collision_helper_4.py"
ADDON_NAME = (
    f"IRE_collision_helper v{VERSION[0]}.{VERSION[4]}.{VERSION[2]}"
)

bl_info = {
    "name": "IRE collider ",
    "author": "Wilkey",
    "version": (0, 0, 1),
    "blender": (4, 1, 0),
    "location": "3D Viewport > Sidebar > My Custom Panel category",
    "description": "for use when adding the custom properties to collision objects for export in IRE  made in 4.1 probably okay for older version ",
    "category": "Development",
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
