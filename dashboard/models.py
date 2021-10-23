from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
import uuid

# START OF CUSTOM USER MODEL


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        default="test@gmail.com"
    )
    name = models.TextField(null=True)
    sap = models.TextField(
        null=True, default="00000000000", max_length=11, unique=True)
    dob = models.DateField(null=True)
    phone = models.TextField(null=True, max_length=10)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    def get_name(self):
        return self.email

    def get_sap(self):
        return self.sap

    def get_phone(self):
        return self.phone

    def get_dob(self):
        return self.dob

    def __str__(self):
        return self.email

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
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin
    objects = UserManager()
# END OF CUSTOM USER MODEL

# START OF SUBJECT, BRANCH, ASSIGNMENT MODELS


class Subject(models.Model):
    subject_name = models.TextField(null=True, unique=True)
    subject_id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def get_subject_name(self):
        return self.subject_name

    class Meta:
        verbose_name_plural = "Subjects"


class Branch(models.Model):
    sap = models.ForeignKey(
        User, to_field='sap', on_delete=models.CASCADE, default="00000000000", max_length=11)
    branch_name = models.TextField(default="BRANCH", unique=True)
    branch_id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True)

    def get_branch_name(self):
        return self.branch_name

    class Meta:
        verbose_name_plural = "Branch"


class Assignments(models.Model):
    branch_id = models.ForeignKey(
        Branch, to_field='branch_id', on_delete=models.CASCADE, default=uuid.uuid4)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assignment_name = models.TextField(default="Assignment")
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    submission_date = models.DateTimeField(null=True)

    def get_assignment_name(self):
        return self.assignment_name

    def get_assignment_status(self):
        return self.status

    def get_submission_date(self):
        return self.submission_date

    def get_subject_id(self):
        return self.subject_id

    class Meta:
        verbose_name_plural = "Assignments"

# END OF SUBJECT, BRANCH, ASSIGNMENT MODELS

# START OF FACULTY MODEL


class Faculty(models.Model):
    faculty_name = models.TextField(null=True, default="NAME")
    faculty_id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    faculty_email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        default="test@gmail.com"
    )

    class Meta:
        verbose_name_plural = "Faculty"
# END OF FACULTY MODEL

# START OF ANNOUNCEMENT MODEL


class Announcements(models.Model):
    announcement_name = models.TextField(null=True, default="Announcement")

    class Meta:
        verbose_name_plural = "Announcement"

# END OF ANNOUNCEMENT MODEL
