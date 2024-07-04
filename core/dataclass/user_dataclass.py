from dataclasses import dataclass
from datetime import datetime


class RolesDataClass:
    seller: bool


@dataclass
class UserDataClass:
    id: int
    email: str
    password: str
    last_login: datetime
    created_at: datetime
    updated_at: datetime
    is_active: bool
    is_superuser: bool
    is_staff: bool
    roles: RolesDataClass


@dataclass
class RolesDataClass:
    id: int


@dataclass
class ProfileDataClass:
    id: int
    name: str
    surname: str
    phone_number: int
    company_name: str
    position: str
    user: UserDataClass


@dataclass
class CarDataClass:
    id: int
    brand: str
    cars_model: str
    seller: UserDataClass
