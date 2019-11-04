from django.contrib.auth import get_user_model
from django.db import models

from core.common.service import ModelServiceMixin
from core.university.managers import (
    FacultyManager,
    DepartmentManager,
    AcademicGroupManager,
    StudentManager,
    TeacherManager,
)
from core.university.services import (
    FacultyService,
    DepartmentService,
    AcademicGroupService,
    StudentService,
    TeacherService,
)

User = get_user_model()


class Faculty(models.Model, ModelServiceMixin):
    name = models.CharField(max_length=50)

    objects = FacultyManager()
    service_class = FacultyService

    def __str__(self):
        return self.name


class Department(models.Model, ModelServiceMixin):
    name = models.CharField(max_length=50)
    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.SET_NULL,
        related_name='departments',
        null=True,
        blank=True
    )

    objects = DepartmentManager()
    service_class = DepartmentService

    def __str__(self):
        return self.name


class AcademicGroup(models.Model, ModelServiceMixin):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()  # TODO add validators
    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE,
        related_name='groups'
    )

    objects = AcademicGroupManager()
    service_class = AcademicGroupService

    def __str__(self):
        return f'{self.name} ({self.year}) - {self.faculty}'


class Student(User):
    group = models.ForeignKey(
        AcademicGroup,
        on_delete=models.CASCADE,
        related_name='students'
    )

    objects = StudentManager()
    service_class = StudentService

    def __str__(self):
        return super(Student, self).__str__() + f' [{self.group}]'


class Teacher(User):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='teachers'
    )

    objects = TeacherManager()
    service_class = TeacherService

    def __str__(self):
        return super(Teacher, self).__str__() + f' [{self.department}]'
