from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


def validation_phone(phone: str):
    if len(phone) == 12 and phone.startswith('+7'):
        for i in range(1, len(phone)):
            if phone[i].isdigit():
                continue
            else:
                raise ValidationError(
                    ("%(phone)s is not phone"),
                    params={"phone": phone},
                )


    else:
        raise ValidationError(
            ("%(phone)s is not number"),
            params={"phone": phone},
        )


class MyUserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone:
            raise ValueError("Users must have an email address")

        user = self.model(
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone=phone,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        null=True
    )
    phone = models.CharField(
        verbose_name="Телефон",
        max_length=12,
        unique=True,
        validators=[validation_phone]
    )
    patronymic = models.CharField(
        verbose_name='Отчество',
        max_length=50,
        null=True
    )
    date_of_birth = models.DateField(blank=True, null=True)
    course = models.ForeignKey(to="Category_course", on_delete=models.CASCADE, verbose_name="course", null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, default='man')
    country = models.CharField(
        max_length=20,
        verbose_name='Страна',
        null=True
    )
    region = models.CharField(
        max_length=50,
        verbose_name='Регион',
        null=True
    )
    locality = models.CharField(
        max_length=40,
        verbose_name='Населеный пункт',
        null=True
    )
    avatar = models.FileField(
        upload_to="Avatar",
        null=True
    )
    objects = MyUserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.phone} | {self.course}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Category_course(models.Model):
    name = models.CharField(max_length=25, verbose_name="category_name")

    def __str__(self):
        return f"{self.name}"
