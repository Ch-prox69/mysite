from django.db import models

class Question(models.Model):
    name = models.CharField(max_length=100)
    question_text = models.TextField()
    answer_text = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question by {self.name}"
