from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, password, **extra_fields):
        for field, value in extra_fields.items():
            if value is None and field != 'profile_image':
                print(value, field)
                raise TypeError("Users must have a {field}".format(
                    field=field
                ))
        user = self.model(**extra_fields)
        user.set_password(password)

        user.save()
        return user

    def create_superuser(self, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(password, **extra_fields)
