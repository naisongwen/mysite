import datetime
from haystack import indexes
from .models import Product


class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    #如果使用一个字段设置了document=True，则一般约定此字段名为text
    text = indexes.CharField(document=True, use_template=True)
    id = indexes.IntegerField(model_attr='id')
    
    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
