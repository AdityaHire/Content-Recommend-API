from django.db import models

class Content(models.Model):
    CATEGORY_CHOICES = [
        ('sports', 'Sports'),
        ('technology', 'Technology'),
        ('entertainment', 'Entertainment'),
        ('news', 'News'),
        ('education', 'Education'),
    ]

    title = models.CharField(max_length=255, help_text="Title of the content")
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        db_index=True,
        help_text="Content Category"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Content"
        verbose_name_plural = "Contents"

    def __str__(self):
        return f"{self.title} ({self.category})"