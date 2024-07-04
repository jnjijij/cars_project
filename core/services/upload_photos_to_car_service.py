import os
from uuid import uuid1

from core.dataclass.user_dataclass import CarDataClass


def upload_photos_to_car(instance, file_name: str) -> str:
    ext = file_name.split('.')[-1]
    return os.path.join('cars', f'{instance.car.id}', f'{uuid1()}.{ext}')
    # return os.path.join(instance.user.email, 'cars', f'{instance.car.id}', f'{uuid1()}.{ext}')
