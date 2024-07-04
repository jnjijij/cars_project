import os
from uuid import uuid1


def upload_avatar(instance, filename: str) -> str:
    ext = filename.split('.')[-1]
    return os.path.join(instance.user.email, 'avatar', f'{uuid1}.{ext}')
