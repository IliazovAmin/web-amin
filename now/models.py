from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    # ваш код модели, если есть

    class Meta:
        # ваш код метаданных
        pass

    # Исправленные обратные связи для полей groups и user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_set'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_set'
    )


class SpeedcubingResult(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    time_in_seconds = models.FloatField()


from django.db import models
from django.contrib.auth import get_user_model

class TimerResult(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    time_elapsed = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.time_elapsed}"


class SpeedcubingResult(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    time_in_seconds = models.FloatField()
    milliseconds = models.IntegerField(default=0)
    seconds = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)