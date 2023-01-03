import os
from . import LOGGER
from werkzeug.utils import secure_filename


def clear_dir(path: str):
    """Clean all the files from directory and its subdirectories

    Args:
        path (str): path to root directory
    """

    for root, dirs, files in os.walk(path, topdown=False):

        for name in files:
            LOGGER.debug(f'removed file path: {os.path.join(root, secure_filename(name))}')
            os.remove(os.path.join(root, secure_filename(name)))

        for name in dirs:
            LOGGER.debug(f'removed directory path: {os.path.join(root, secure_filename(name))}')
            os.rmdir(os.path.join(root, secure_filename(name)))