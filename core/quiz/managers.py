from django.db.models import QuerySet, Manager


class QuizQuerySet(QuerySet):
    pass


class QuizSetQuerySet(QuerySet):
    pass


class QuestionQuerySet(QuerySet):
    pass


class AnswerQuerySet(QuerySet):
    pass


class GroupQuizQuerySet(QuerySet):
    pass


class StudentQuizQuerySet(QuerySet):
    pass


class StudentQuestionQuerySet(QuerySet):
    pass


class QuizManager(Manager):
    _queryset_class = QuizQuerySet


class QuizSetManager(Manager):
    _queryset_class = QuizSetQuerySet


class QuestionManager(Manager):
    _queryset_class = QuestionQuerySet


class AnswerManager(Manager):
    _queryset_class = AnswerQuerySet


class GroupQuizManager(Manager):
    _queryset_class = GroupQuizQuerySet


class StudentQuizManager(Manager):
    _queryset_class = StudentQuizQuerySet


class StudentQuestionManager(Manager):
    _queryset_class = StudentQuestionQuerySet

