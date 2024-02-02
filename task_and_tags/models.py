from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self) -> str:
        return self.name

class Tasks(models.Model):
    content = models.TextField()
    datetime = models.DateField()
    done_task_until_date = models.DateField(blank=True)
    task_is_done = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tags")

    class Meta:
        ordering = ["task_is_done"]

    def __str__(self) -> str:
        return self.content
