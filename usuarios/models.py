from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
    Group,
    Permission,
)


class UsuarioManager(BaseUserManager):

    def create_user(self, email, password=None):
        usuario = self.model(
            email=self.normalize_email(email)
        )

        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)

        usuario.save()

        return usuario

    def create_superuser(self, email, password):
        usuario = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )

        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        return usuario


class Usuario(AbstractBaseUser, PermissionsMixin):

    groups = models.ManyToManyField(
        Group,
        related_name='usuarios',
        verbose_name=_('grupos'),
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuarios',
        verbose_name=_('permissões do usuário'),
        blank=True,
    )

    email = models.EmailField(
        verbose_name="E-mail do usuário",
        max_length=194,
        unique=True,
    )

    is_active = models.BooleanField(
        verbose_name="Usuário está ativo",
        default=True,
    )

    is_staff = models.BooleanField(
        verbose_name="Usuário é da equipe de desenvolvimento",
        default=False,
    )

    is_superuser = models.BooleanField(
        verbose_name="Usuário é um superusuario",
        default=False,
    )

    USERNAME_FIELD = 'email'

    objects = UsuarioManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        db_table = 'usuario'

    def __str__(self):
        return self.email
