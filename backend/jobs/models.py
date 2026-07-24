"""Models do app jobs."""
import uuid

from django.conf import settings
from django.db import models


class JobPosting(models.Model):
    """
    Raw job posting content submitted by a candidate for comparison
    against their resume.
    """

    class Source(models.TextChoices):
        PDF = "pdf", "PDF"
        TEXT = "text", "Text"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    submitted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="job_postings",
        db_column="submitted_by",
    )
    source = models.CharField(
        max_length=10,
        choices=Source.choices,
        help_text="pdf or text",
    )
    raw_text = models.TextField(
        blank=True,
        null=True,
    )
    file_url = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Set when source is pdf, stored on Supabase",
    )
    extracted_text = models.TextField(
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "job_postings"
        ordering = ["-created_at"]
        verbose_name = "Job Posting"
        verbose_name_plural = "Job Postings"

    def __str__(self):
        return f"JobPosting({self.id}) - {self.source}"