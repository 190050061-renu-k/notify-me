from django.db import models, transaction
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):

    def _create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given email,and password.
        """
        if not username:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(username=username, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(username, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=40, unique=True)
    username = models.CharField(max_length=60, blank=True, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    date_joined=models.DateField(default=timezone.now)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="student_account", default=User.objects.filter(is_student="True"))
    registration_token=models.CharField(max_length=400, blank=True)

    def __str__(self):
        return self.user.username


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="instructor_account")

    def __str__(self):
        return self.user.username


class Course(models.Model):
    code = models.CharField(default='', max_length=10, primary_key=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True)
    date = models.DateTimeField(default=timezone.now)
    name = models.CharField(default='', max_length=100)

    def __str__(self):
        return self.name


class Deadline(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
    end_date=models.DateTimeField()
    message = models.CharField(default='', max_length=500)
    hard=models.BooleanField(default=False)

    def __str__(self):
        return self.message
