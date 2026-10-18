import uuid
from typing import Any

from django.db import models
from django.utils.text import slugify
from django_stubs_ext.db.models.manager import RelatedManager
from unidecode import unidecode


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Quiz(BaseModel):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    about = models.TextField()
    questions: RelatedManager[Question]

    def save(self, *args: Any, **kwargs: Any) -> None:
        if not self.slug:
            self.slug = slugify(unidecode(self.title)) or "quiz"
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class Question(BaseModel):
    quiz = models.ForeignKey(Quiz, related_name="questions", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    marks = models.IntegerField(default=5)
    answers: RelatedManager[Answer]

    def __str__(self) -> str:
        return self.title


class Answer(BaseModel):
    question = models.ForeignKey(
        Question, related_name="answers", on_delete=models.CASCADE
    )
    option = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.option
