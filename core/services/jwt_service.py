from typing import Type

from django.contrib.auth import get_user_model

from rest_framework.generics import get_object_or_404

from rest_framework_simplejwt.tokens import BlacklistMixin, Token

from apps.all_users.users.models import UserModel as User

UserModel: User = get_user_model()
from core.enums.action_token_enum import ActionTokenEnum

ActionTokenClassType = Type[BlacklistMixin | Token]


class ActionToken(Token, BlacklistMixin):
    pass


class ActivateToken(ActionToken):
    token_type = ActionTokenEnum.ACTIVATE.token_type
    lifetime = ActionTokenEnum.ACTIVATE.life_time


class RecoveryToken(ActionToken):
    token_type = ActionTokenEnum.RECOVERY.token_type
    lifetime = ActionTokenEnum.RECOVERY.life_time


class JWTService:
    @staticmethod
    def create_token(user, token_class: ActionTokenClassType):
        return token_class.for_user(user)

    @staticmethod
    def validate_token(token, token_class: ActionTokenClassType):
        try:
            token_result = token_class(token)
            token_result.check_blacklist()
        except Exception as err:
            print(err)
        token_result.blacklist()
        user_id = token_result.payload.get('user_id')
        return get_object_or_404(UserModel, pk=user_id)
