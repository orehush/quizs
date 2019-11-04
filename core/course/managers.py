from django.db.models import QuerySet, Manager


class TeamQuerySet(QuerySet):
    pass


class TeamMemberQuerySet(QuerySet):
    pass


class CourseQuerySet(QuerySet):
    pass


class TeamManager(Manager):
    _queryset_class = TeamQuerySet


class TeamMemberManager(Manager):
    _queryset_class = TeamMemberQuerySet


class CourseManager(Manager):
    _queryset_class = CourseQuerySet
