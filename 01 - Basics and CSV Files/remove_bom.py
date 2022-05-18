import codecs
import os

def remove_bom_inplace(path):
    """Removes BOM mark, if it exists, from a file and rewrites it in-place
    Parameters
    ----------
    path : str
        path to file requireing bom removal
    """
    buffer_size = 4096
    bom_length = len(codecs.BOM_UTF8)
    with open(path, "r+b") as fp:
        chunk = fp.read(buffer_size)
        if chunk.startswith(codecs.BOM_UTF8):
            i = 0
            chunk = chunk[bom_length:]
            while chunk:
                fp.seek(i)
                fp.write(chunk)
                i += len(chunk)
                fp.seek(bom_length, os.SEEK_CUR)
                chunk = fp.read(buffer_size)
            fp.seek(-bom_length, os.SEEK_CUR)
            fp.truncate()