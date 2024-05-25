from django.db import models
import hashlib
from django.utils import timezone

class ShortLink(models.Model):
    original_url = models.URLField()
    hash_value = models.CharField(max_length=10, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)  # Soft delete flag

    def save(self, *args, **kwargs):
        if not self.hash_value:
            self.hash_value = hashlib.md5(self.original_url.encode()).hexdigest()[:10]
        super().save(*args, **kwargs)

    @property
    def short_url(self):
        return f"http://localhost:8000/short-links/{self.hash_value}"

    def __str__(self):
        return f"{self.original_url} -> {self.short_url}"
