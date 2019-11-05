from django.db import models
from django.utils.text import Truncator

from core.common.service import ModelServiceMixin
from core.quiz.managers import (
    QuestionManager,
    QuizSetManager,
    QuizManager,
    AnswerManager,
    GroupQuizManager,
    StudentQuizManager,
    StudentQuestionManager,
)
from core.quiz.services import (
    StudentQuestionService,
    StudentQuizService,
    GroupQuizService,
    AnswerService,
    QuestionService,
    QuizSetService,
    QuizService,
)


class Quiz(models.Model, ModelServiceMixin):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(
        'course.Course',
        on_delete=models.CASCADE,
        related_name='quizzes'
    )

    objects = QuizManager()
    service_class = QuizService

    def __str__(self):
        return self.name


class QuizSet(models.Model, ModelServiceMixin):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='sets'
    )

    objects = QuizSetManager()
    service_class = QuizSetService


class Question(models.Model, ModelServiceMixin):
    text = models.TextField(max_length=1000)
    quiz_set = models.ForeignKey(
        QuizSet,
        on_delete=models.CASCADE,
        related_name='questions'
    )

    objects = QuestionManager()
    service_class = QuestionService

    def __str__(self):
        return Truncator(self.text).words(5)


class Answer(models.Model, ModelServiceMixin):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers'
    )
    text = models.TextField(max_length=200)
    is_right = models.BooleanField(default=False)

    objects = AnswerManager()
    service_class = AnswerService

    def __str__(self):
        return Truncator(self.text).words(5)


class GroupQuiz(models.Model, ModelServiceMixin):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='groups'
    )
    group = models.ForeignKey(
        'university.AcademicGroup',
        on_delete=models.CASCADE,
        related_name='quizzes'
    )
    status = models.PositiveSmallIntegerField(
        choices=()  # TODO add choices
    )

    objects = GroupQuizManager()
    service_class = GroupQuizService


class StudentQuiz(models.Model, ModelServiceMixin):
    group_quiz = models.ForeignKey(
        GroupQuiz,
        on_delete=models.CASCADE,
        related_name='student_quizzes'
    )
    student = models.ForeignKey(
        'university.Student',
        on_delete=models.CASCADE,
        related_name='student_quizzes'
    )
    status = models.PositiveSmallIntegerField(
        choices=()  # TODO add choices
    )

    objects = StudentQuizManager()
    service_class = StudentQuizService


class StudentQuestion(models.Model, ModelServiceMixin):
    student_quiz = models.ForeignKey(
        StudentQuiz,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='student_questions'
    )
    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE,
        related_name='student_answers',
        null=True,
        blank=True
    )
    status = models.PositiveSmallIntegerField(
        choices=()  # TODO add choices
    )

    objects = StudentQuestionManager()
    service_class = StudentQuestionService
