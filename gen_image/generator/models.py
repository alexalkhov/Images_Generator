from django.db import models


class GeneratedImage(models.Model):
    model = models.CharField(max_length=255)
    prompt = models.CharField(max_length=255)
    negative_prompt = models.CharField(max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()
    result = models.ImageField(
        upload_to='generated_images/',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Generated Image {self.id}"
