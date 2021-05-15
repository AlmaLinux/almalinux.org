import hashlib
from os import path

from django.db.models import Model


# This method allows for file uploads to live in segmented folders,
# instead of placing all uploads in a single folder.
# noinspection PyUnusedLocal
def segmented_upload_to(instance: Model, file_name: str) -> str:
    """
    :param instance:
    :param file_name: string
    """
    filename_base, filename_ext = path.splitext(file_name)
    filename_base = filename_base.replace('/', '_')
    hashcode = hashlib.md5(filename_base.encode()).hexdigest()

    return '{0}/{1}/{2}/{3}{4}'.format(
        hashcode[0:2],
        hashcode[2:4],
        hashcode[4:6],
        filename_base,
        filename_ext
    )
