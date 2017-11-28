from django.db import models

# Create your models here.


class Benke(models.Model):
    liuxue_leixing_choice=(
        ('国内高中申请国外10-12年级高中', '国内高中申请国外10-12年级高中'),
        ('国内高中申请国外大学预备课程', '国内高中申请国外大学预备课程'),
        ('国内高中申请国外大学本科', '国内高中申请国外大学本科'),
        ('国内高中申请国外大学学分转换课程', '国内高中申请国外大学学分转换课程'),
        ('国内高中申请国外大学副学士/Diploma课程', '国内高中申请国外大学副学士/Diploma课程'),
        ('国内高中申请合作办学课程', '国内高中申请合作办学课程'),
        ('国内高中申请境内国外10-12年级课程', '国内高中申请境内国外10-12年级课程'),
        ('国内高中申请境内大学预备课程', '国内高中申请境内大学预备课程'),
        ('国内高中申请境内国外大学学分转换课程', '国内高中申请境内国外大学学分转换课程'),
        ('国外高中申请国外副学士/Diploma课程', '国外高中申请国外副学士/Diploma课程'),
        ('国外高中申请国外大学本科课程', '国外高中申请国外大学本科课程'),
    )
    xuexiao_leibie_choice=(
        ('国内重点高中/实验班', '国内重点高中/实验班'),
        ('普通国际学校高中部', '普通国际学校高中部'),
        ('普通高中', '普通高中'),
        ('海外学校', '海外学校'),
    )
    xueli_leibie_choice=(
        ('中国高中课程', '中国高中课程'),
        ('中国高中和海外高中混合课程', '中国高中和海外高中混合课程'),
        ('海外高中课程', '海外高中课程'),
    )
    guojia = models.CharField("国家", max_length=20, default="美国")
    liuxue_leixing = models.CharField("留学项目申请", max_length=50, choices=liuxue_leixing_choice, default='国内高中申请国外大学本科')
    zhongwen = models.CharField("录取学校（中文）", max_length=200)
    xuezhi = models.IntegerField("学制", blank=True, null=True, default=4)
    jiangxuejin = models.IntegerField("奖学金", blank=True, null=True)
    zhuanye = models.CharField("录取专业", max_length=100)
    chengshi = models.CharField("学员城市", max_length=50, blank=True, null=True)
    xuexiaoleibie = models.CharField("学员学校类别", max_length=50, choices=xuexiao_leibie_choice, default='国内重点高中/实验班')
    xueli = models.CharField("申请学历", max_length=50, default="本科")
    xueli_leibie = models.CharField("就读学历类别", max_length=50, choices=xueli_leibie_choice, default='中国高中课程')
    jigou = models.CharField("代理机构", max_length=50)
    jigou_city = models.CharField("代理城市", max_length=50)
    gpa = models.FloatField()
    url = models.URLField(blank=True, null=True)
    offer_huoqu = models.CharField("Offer获取时间", max_length=20, blank=True, null=True, default="2016年3月")
    xuexiao = models.CharField("学员学校", max_length=50, blank=True, null=True)
    xueli_chengdu = models.CharField("就读学历程度", max_length=50, blank=True, null=True, default="12年级完成")
    gaokao = models.CharField("高考成绩", max_length=20, blank=True, null=True)
    ielts = models.FloatField(blank=True, null=True)
    sat = models.IntegerField(blank=True, null=True)
    tofel = models.IntegerField(blank=True, null=True)
    act = models.IntegerField(blank=True, null=True)
    tiaojian = models.CharField("录取条件", max_length=50, blank=True, null=True, default="Full Offer")
    p = models.IntegerField("发布", blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'benke'
        verbose_name = '本科Offer'
        verbose_name_plural = '本科Offers'

class Shuoshi(models.Model):
    liuxue_leixing = models.CharField(max_length=50)
    zhongwen = models.CharField(max_length=200)
    xuezhi = models.IntegerField(blank=True, null=True)
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
    url = models.URLField(blank=True, null=True)
    offer_huoqu = models.CharField(max_length=20, blank=True, null=True)
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