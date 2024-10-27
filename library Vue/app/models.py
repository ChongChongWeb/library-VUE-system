from django.db import models

# 图书类型
class BookTypes(models.Model):

    id=models.AutoField('记录ID', primary_key=True)
    name=models.CharField('类型名称', max_length=20, null=False)

    class Meta:
        db_table='fater_book_types'


# 图书信息
class BookInfos(models.Model):

    id = models.AutoField('记录ID', primary_key=True)
    img = models.ImageField('图书配图', upload_to='static/imgs', max_length=125)
    name = models.CharField('图书名称', max_length=20, null=False)
    price = models.FloatField('图书价格', null=False)
    intro = models.CharField('图书介绍', max_length=256, null=False)
    type = models.ForeignKey(BookTypes, db_column='type_id', null=False, on_delete=models.CASCADE)

    class Meta:
        db_table='fater_book_infos'
