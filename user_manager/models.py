from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    TYPE_CHOICE = (
        ('s' , 'Student'),
        ('d' , 'Doctor'),
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICE)

    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Hostel(models.Model):
    hostel_name = models.CharField(max_length=100)
    dean_name = models.CharField(max_length=100)
    hostel_add = models.CharField(max_length=600)
    dean_mobile_number = models.CharField(max_length=100)
    dean_email = models.EmailField(max_length=100)

    def __str__(self):
        return str(self.hostel_name)


class DoctorProfile(models.Model):
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_doctor')
    specialization = models.CharField(max_length=100)
    mobiles_number = models.CharField(max_length=100)
    address = models.CharField(max_length=500)

    def __str__(self):
        return str(self.doctor)


class StudentProfile(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_student')
    hostel = models.ForeignKey(Hostel, on_delete=models.SET_NULL, related_name='hostel_student', null=True)
    assigned_doctor = models.ForeignKey(DoctorProfile, on_delete=models.SET_NULL, related_name='student_doctor_profile', null=True)
    birthdate = models.DateField()
    GENDER_CHOICE = (
        ('m' , 'male'),
        ('f' , 'female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    parent_email = models.EmailField(max_length=100)

    def __str__(self):
        return str(self.student)


