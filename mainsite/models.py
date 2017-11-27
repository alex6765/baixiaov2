from django.db import models

# Create your models here.


class Benke(models.Model):
    liuxue_leixing = models.CharField(max_length=50)
    zhongwen = models.CharField(max_length=200)
    jiangxuejin = models.IntegerField(blank=True, null=True)
    zhuanye = models.CharField(max_length=100)
    chengshi = models.CharField(max_length=50, blank=True, null=True)
    xuexiaoleibie = models.CharField(max_length=50)
    xueli = models.CharField(max_length=50)
    xueli_leibie = models.CharField(max_length=50)
    jigou = models.CharField(max_length=50)
    jigou_city = models.CharField(max_length=50)
    gpa = models.FloatField()
    url = models.CharField(max_length=2000, blank=True, null=True)
    offer_huoqu = models.CharField(max_length=20, blank=True, null=True)
    xuezhi = models.IntegerField(blank=True, null=True)
    xuexiao = models.CharField(max_length=50, blank=True, null=True)
    xueli_chengdu = models.CharField(max_length=50, blank=True, null=True)
    gaokao = models.CharField(max_length=20, blank=True, null=True)
    ielts = models.FloatField(blank=True, null=True)
    sat = models.IntegerField(blank=True, null=True)
    tofel = models.IntegerField(blank=True, null=True)
    act = models.IntegerField(blank=True, null=True)
    tiaojian = models.CharField(max_length=50, blank=True, null=True)
    p = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'benke'

class Shuoshi(models.Model):
    liuxue_leixing = models.CharField(max_length=50)
    zhongwen = models.CharField(max_length=200)
    jiangxuejin = models.IntegerField(blank=True, null=True)
    zhuanye = models.CharField(max_length=100)
    chengshi = models.CharField(max_length=50, blank=True, null=True)
    xuexiaoleibie = models.CharField(max_length=50)
    xueli = models.CharField(max_length=50)
    xueli_leibie = models.CharField(max_length=50)
    zhuanye_ch = models.CharField(max_length=100)
    jigou = models.CharField(max_length=50)
    jigou_city = models.CharField(max_length=50)
    gpa = models.FloatField()
    url = models.CharField(max_length=2000, blank=True, null=True)
    offer_huoqu = models.CharField(max_length=20, blank=True, null=True)
    xuezhi = models.IntegerField(blank=True, null=True)
    xuexiao = models.CharField(max_length=50, blank=True, null=True)
    xueli_chengdu = models.CharField(max_length=50, blank=True, null=True)
    ielts = models.FloatField(blank=True, null=True)
    tofel = models.IntegerField(blank=True, null=True)
    gre = models.IntegerField(blank=True, null=True)
    gmat = models.IntegerField(blank=True, null=True)
    tiaojian = models.CharField(max_length=50, blank=True, null=True)
    p = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shuoshi'