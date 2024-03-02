from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, password = None):
        
        user = self.model(
            username = username,
            email = email,
            first_name=first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, username, email, first_name, last_name, password = None):

        user = self.create_user(
            username = username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    


class MyUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        max_length=50,
        verbose_name='Имя пользователя',
        unique=True,
    )
    first_name = models.CharField(
        max_length=155,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=155,
        verbose_name='Фамилия'
    )
    created_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активен'
    )
    is_staff = models.BooleanField(
        default=True,
        verbose_name='Сотрудник'
    )
    is_admin = models.BooleanField(
        default=False,
        verbose_name='Админ'
    )
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_myuser_set',  # измененное related_name
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_myuser_set',  # измененное related_name
        related_query_name='user',
        help_text='Specific permissions for this user.',
    )
    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username
