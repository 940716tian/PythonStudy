from django.contrib.auth.backends import ModelBackend

from .models import MyUser


class MyBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # 找人
        try:
            user = MyUser.objects.get(username=username)
        except Exception:
            try:
                user = MyUser.objects.get(phone=username)
            except Exception:
                return None

        # 密码校验
        if user.check_password(password):
            return user
        else:
            return None