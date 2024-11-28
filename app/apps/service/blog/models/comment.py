from django.db import models
from django.contrib.auth import get_user_model

from utils.models.base_model import BaseModel
from .blog import Blog

User = get_user_model()


class Comment(BaseModel):
    content= models.TextField(
        'Bloq rəyi'
    )
    blog = models.ForeignKey(
        Blog, 
        on_delete=models.CASCADE, 
        related_name='comments',
        verbose_name='Bloq'
    )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='comments',
        verbose_name='Rəy müəllifi'
    )

    class Meta:
          verbose_name = ('Məqalə rəyi')
          verbose_name_plural = ('Məqalə rəyləri')
          ordering = ['-created_at']
          indexes = [
            models.Index(fields=['-created_at'])
        ]
            
    @property
    def truncated_comment(self):
        max_words = 3
        words = self.content.split()
        truncated_words = words[:max_words]
        truncated_content = ' '.join(truncated_words)

        if len(words) > max_words:
            truncated_content += ' ...'  

        return truncated_content

    def __str__(self) -> str:
        return self.truncated_comment