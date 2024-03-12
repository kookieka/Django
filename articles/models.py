from django.db import models

# Create your models here.
# models.Model : 데이터베이스(DB)의 테이블
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        # 눈에 보이는 게시글은 pk(고유번호)와 title로 구성
        return f'[{self.pk} {self.title}]'
