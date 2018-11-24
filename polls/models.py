from django.db import models
from DjangoUeditor.models import UEditorField
import django.utils.timezone as timezone
from django.forms import ModelForm


# Create your models here.


class MainManu(models.Model):
    title=models.CharField(max_length=100,verbose_name='一级分类菜单标题')
    tempalte_choice=(
	('AD','article_detail'),
	('AL','article_list'),
	('PL','product_list')
    )
    template=models.CharField(max_length=100,choices=tempalte_choice,verbose_name='展示模版',null=True)

    def __str__(self):
        return self.title
    
    class Meta:
         verbose_name = "一级分类菜单"
         verbose_name_plural = "一级分类菜单"

class SecondaryManu(models.Model):
    #To define a many-to-one relationship, use django.db.models.ForeignKey
    mainmanu=models.ForeignKey(MainManu,on_delete=models.CASCADE,verbose_name='请设置一级分类')
    title=models.CharField(max_length=100,verbose_name='二级分类菜单标题')
    cover_image = models.ImageField(upload_to='products',verbose_name='封面图',null=True)

    def __str__(self):
        return self.title

    class Meta:
         verbose_name = "二级分类菜单"
         verbose_name_plural = "二级分类菜单"

class Article(models.Model):
    title=models.CharField(max_length=100,blank=True,verbose_name='标题')
    mainmanu=models.ForeignKey(MainManu,on_delete=models.CASCADE,null=True,verbose_name='请设置一级分类')
    secondarymanu=models.ForeignKey(SecondaryManu,on_delete=models.CASCADE,null=True,verbose_name='请设置二级分类')
    #secondaryCategory=forms.ModelChoiceField(queryset =SecondaryManu.objects.all(),empty_label='请设置二级分类')
    pub_date = models.DateTimeField('date published',default = timezone.now)
    update_date = models.DateTimeField('date updated',auto_now = True)
    content=UEditorField(u'内容	',width=600, height=300, toolbars="full", imagePath="images/", filePath="", upload_settings={"imageMaxSize":1204000},
 settings={},blank=True)

    def __str__(self):
        return self.title

    class Meta:
         verbose_name = "资讯内容页"
         verbose_name_plural = "资讯内容页"

class Product(models.Model):
    title=models.CharField(max_length=100,blank=True,verbose_name='标题')
    mainmanu=models.ForeignKey(MainManu,on_delete=models.CASCADE,null=True,verbose_name='选择一级类目')
    secondarymanu=models.ForeignKey(SecondaryManu,on_delete=models.CASCADE,null=True,verbose_name='选择二级类目')
    mainPhoto = models.ImageField(upload_to='products',verbose_name='上传主图')
    pub_date = models.DateTimeField('发布日期',default = timezone.now)
    update_date = models.DateTimeField('更新日期',auto_now = True)
    content=UEditorField(u'内容',width=600, height=300, toolbars="full", imagePath="images/", filePath="", upload_settings={"imageMaxSize":1204000},
 settings={},blank=True)

    def __str__(self):
        return self.title

    class Meta:
         verbose_name = "产品内容页" 
         verbose_name_plural = "产品内容页"

class Consult (models.Model):
    name = models.CharField(verbose_name='姓名', max_length=20)
    telphone = models.CharField(verbose_name='电话', max_length=20)
    email = models.EmailField(verbose_name='邮箱', max_length=254)
    remark = models.TextField(verbose_name='备注', max_length=1000)

    def __str__(self):
        return self.remark

    class Meta:
         verbose_name = "客户咨询" 
         verbose_name_plural = "客户咨询"

class CustomerAppraise (models.Model):
    customer_name = models.CharField(verbose_name='客户名称', max_length=100,null=True)
    customer_logo = models.ImageField(verbose_name='客户LOGO',upload_to='customers')
    customer_appraise= models.CharField(verbose_name='评价内容', max_length=2000)
    appraise_date = models.DateTimeField('评价时间',default = timezone.now)
 
    def __str__(self):
        return self.customer_appraise
   
    class Meta:
        verbose_name = "客户评价"
        verbose_name_plural = "客户评价"

class RotateImage (models.Model):
    rotate_image = models.ImageField(verbose_name='首页滚屏图片',upload_to='images',null=True)
    rotate_title = models.CharField(verbose_name='图片标题', max_length=300,null=True)
    rotate_link = models.CharField(verbose_name='跳转地址', max_length=300,null=True)

    def __str__(self):
        return self.rotate_link

    class Meta:
        verbose_name = "首页滚屏图像"
        verbose_name_plural = "首页滚屏图像"

class FAQ (models.Model):
    question=models.CharField(verbose_name='问题描述', max_length=200)
    answer=models.CharField(verbose_name='问题答案', max_length=400)
    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "常见问题"
        verbose_name_plural = "常见问题"

class ConsultForm(ModelForm):
    class Meta:
        model=Consult
        fields=['name','telphone','email','remark']

