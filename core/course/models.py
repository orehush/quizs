from django.db import models
from django_extensions.db.models import TimeStampedModel

from core.common.service import ModelServiceMixin
from core.course.managers import (
    CourseManager,
    TeamManager,
    TeamMemberManager,
)
from core.course.services import TeamService, TeamMemberService, CourseService
from core.university.models import Teacher


class Team(models.Model, ModelServiceMixin):
    members = models.ManyToManyField(
        Teacher,
        through='course.TeamMember'
    )

    objects = TeamManager()
    service_class = TeamService

    def __str__(self):
        return f'{self.course}\'s team'


class TeamMember(models.Model, ModelServiceMixin):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='members'
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='teams'
    )
    role = models.PositiveSmallIntegerField(choices=())  # TODO add choices

    objects = TeamMemberManager()
    service_class = TeamMemberService


class Course(TimeStampedModel, ModelServiceMixin):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(
        'university.Department',
        on_delete=models.CASCADE,
        related_name='courses'
    )
    team = models.OneToOneField(
        Team,
        on_delete=models.CASCADE,
        related_name='course'
    )

    objects = CourseManager()
    service_class = CourseService

    def __str__(self):
        return self.name
