'''
mimetypes is blocked by Global Script/ControlScript
This module provides some of the features of mimetypes, but is not complete (not even close, feel free to contribute at https://github.com/GrantGMiller/gs_mimetypes)
'''

try:
    from pathlib import Path
except:
    from gs_pathlib import Path  # https://github.com/GrantGMiller/gs_pathlib


def guess_type(src):
    typ = {
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.gif': 'image/gif',
        '.ico': 'image/x-icon',
        '.jfif': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.txt': 'text/plain',
        '.py': 'text/plain',
        '.mp4': 'video/mp4',
    }[Path(src).suffix.lower()]
    return typ, typ
