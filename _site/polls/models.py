from django.db import models
from DjangoUeditor.models import UEditorField
import django.utils.timezone as timezone

# Create your models here.

class Question(models.Model):
    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
     
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Article(models.Model):
    title=models.CharField(max_length=100,blank=True,verbose_name='标题')
    category=models.CharField(max_length=100,blank=True,verbose_name='类目')
    pub_date = models.DateTimeField('date published',default = timezone.now)
    update_date = models.DateTimeField('date updated',auto_now = True)
    content=UEditorField(u'内容	',width=600, height=300, toolbars="full", imagePath="images/", filePath="", upload_settings={"imageMaxSize":1204000},
 settings={},blank=True)

    def __str__(self):
        return self.title
