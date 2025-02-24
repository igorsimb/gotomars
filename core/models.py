from django.contrib.auth.models import AbstractUser
from django.db import models
from django_prose_editor.fields import ProseEditorField


class User(AbstractUser):
    pass


class Feature(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    content = ProseEditorField()
    is_active = models.BooleanField(default=True, help_text="Максимум 4 активные фичи на странице")

    def __str__(self):
        return self.title if self.title else self.content[:20]
