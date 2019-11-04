from django.db.models import Manager, QuerySet

from core.user.managers import UserQuerySet, UserManager


class FacultyQuerySet(QuerySet):
    pass


class DepartmentQuerySet(QuerySet):
    pass


class AcademicGroupQuerySet(QuerySet):
    pass


class StudentQuerySet(UserQuerySet):
    pass


class TeacherQuerySet(UserQuerySet):
    pass


class FacultyManager(Manager):
    _queryset_class = FacultyQuerySet


class DepartmentManager(Manager):
    _queryset_class = DepartmentQuerySet


class AcademicGroupManager(Manager):
    _queryset_class = AcademicGroupQuerySet


class StudentManager(UserManager):
    _queryset_class = StudentQuerySet


class TeacherManager(UserManager):
    _queryset_class = TeacherQuerySet
