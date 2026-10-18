from django.contrib import admin

from quiztempl.server.apps.quiz.models import Answer, Question, Quiz


@admin.register(Quiz)
class QuizModelAdmin(admin.ModelAdmin[Quiz]):
    exclude = ["slug"]
    fields = ["title", "about"]


@admin.register(Question)
class QuestionModelAdmin(admin.ModelAdmin[Question]):
    pass


@admin.register(Answer)
class AnswerModelAdmin(admin.ModelAdmin[Answer]):
    pass
