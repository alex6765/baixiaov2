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
        ('国际交换生经验申请国外大学本科课程', '国际交换生经验申请国外大学本科课程'),
    )
    xuexiao_leibie_choice=(
        ('国内重点高中/实验班', '国内重点高中/实验班'),
        ('普通国际学校高中部', '普通国际学校高中部'),
        ('海外学校在国内开设的分校', '海外学校在国内开设的分校'),
        ('普通高中', '普通高中'),
        ('海外学校', '海外学校'),
    )
    xueli_leibie_choice=(
        ('中国高中课程', '中国高中课程'),
        ('A LEVEL', 'A LEVEL'),
        ('IB', 'IB'),
        ('中国高中和海外高中混合课程', '中国高中和海外高中混合课程'),
        ('海外高中课程', '海外高中课程'),
    )
    area_choice=(
        ('工程与技术', (
            ('电子电气工程', '电子电气工程'),
            ('化学工程', '化学工程'),
            ('机械，航空及制造工程', '机械，航空及制造工程'),
            ('计算机科学与信息系统', '计算机科学与信息系统'),
            ('矿物与采矿工程', '矿物与采矿工程'),
            ('土木工程与结构工程', '土木工程与结构工程'),
        )
         ),
        ('人文科学与艺术', (
            ('艺术设计', '艺术设计'),
            ('表演艺术', '表演艺术'),
            ('建筑', '建筑'),
            ('考古学', '考古学'),
            ('历史', '历史'),
            ('人类学', '人类学'),
            ('英语语言文学', '英语语言文学'),
            ('语言学', '语言学'),
            ('哲学', '哲学'),
        )
         ),
        ('社会科学与管理', (
            ('传播与媒体研究', '传播与媒体研究'),
            ('发展研究', '发展研究'),
            ('法学', '法学'),
            ('会计与金融', '会计与金融'),
            ('教育学', '教育学'),
            ('经济学与计量经济学', '经济学与计量经济学'),
            ('酒店与休闲管理', '酒店与休闲管理'),
            ('商务与管理研究', '商务与管理研究'),
            ('社会学', '社会学'),
            ('社会政策与管理', '社会政策与管理'),
            ('体育相关学科', '体育相关学科'),
            ('统计学与运营', '统计学与运营'),
            ('政治学与国际研究', '政治学与国际研究'),
        )
         ),
        ('生物科学与医学', (
            ('护理', '护理'),
            ('解剖生理学', '解剖生理学'),
            ('农林', '农林'),
            ('生物科学', '生物科学'),
            ('兽医', '兽医'),
            ('心理学', '心理学'),
            ('牙医', '牙医'),
            ('医学', '医学'),
        )
         ),
        ('自然科学', (
            ('材料科学', '材料科学'),
            ('地理学', '地理学'),
            ('地球与海洋科学', '地球与海洋科学'),
            ('化学', '化学'),
            ('环境科学', '环境科学'),
            ('数学', '数学'),
            ('物理学与天文学', '物理学与天文学'),
        )
         ),
        ('通识教育', '通识教育'),
    )
    guojia = models.CharField("国家", max_length=20, default="美国")
    liuxue_leixing = models.CharField("留学项目申请", max_length=50, choices=liuxue_leixing_choice, default='国内高中申请国外大学本科')
    zhongwen = models.CharField("录取学校（中文）", max_length=200)
    xuezhi = models.IntegerField("学制", blank=True, null=True, default=4)
    jiangxuejin = models.IntegerField("奖学金", blank=True, null=True)
    zhuanye = models.CharField("录取专业", max_length=100)
    area = models.CharField("专业类型", max_length=100, choices=area_choice, default='通识教育')
    chengshi = models.CharField("学员城市", max_length=50, blank=True, null=True)
    xuexiaoleibie = models.CharField("学员学校类别", max_length=50, choices=xuexiao_leibie_choice, default='国内重点高中/实验班')
    xueli = models.CharField("申请学历", max_length=50, default="本科")
    xueli_leibie = models.CharField("就读学历类别", max_length=50, choices=xueli_leibie_choice, default='中国高中课程')
    jigou = models.CharField("代理机构", max_length=50)
    jigou_city = models.CharField("代理城市", max_length=50, default="北京")
    guwen_name = models.CharField("顾问姓名", max_length=50, blank=True, null=True,)
    anli_tese = models.CharField("案例特色", max_length=1000, blank=True, null=True,)
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
    liuxue_leixing_choice=(
        ('国内本科转学国外本科', '国内本科转学国外本科'),
        ('大学预备课程申请本科', '大学预备课程申请本科'),
        ('大学学分课程升海外本科', '大学学分课程升海外本科'),
        ('专科/高职对接国外本科', '专科/高职对接国外本科'),
        ('高教自考/成人高考对接国外本科', '高教自考/成人高考对接国外本科'),
        ('合作办学转学国外本科', '合作办学转学国外本科'),
        ('专科/高职申请国外研究生/硕士课程', '专科/高职申请国外研究生/硕士课程'),
        ('高教自考/成人高考申请研究生/硕士课程', '高教自考/成人高考申请研究生/硕士课程'),
        ('合作办学申请研究生/硕士课程', '合作办学申请研究生/硕士课程'),
        ('国内本科申请国外研究生/硕士课程', '国内本科申请国外研究生/硕士课程'),
        ('海外Diploma/副学士申请本科课程', '海外Diploma/副学士申请本科课程'),
        ('海外Diploma/副学士申请研究生/硕士课程', '海外Diploma/副学士申请研究生/硕士课程'),
        ('海外本科申请研究生/硕士课程', '海外本科申请研究生/硕士课程'),
    )
    xuexiao_leibie_choice=(
        ('重点高校（211，985，一本高校）', '重点高校（211，985，一本高校）'),
        ('合作办学', '合作办学'),
        ('普通高校', '普通高校'),
        ('海外高校', '海外高校'),
        ('留学培训机构', '留学培训机构'),
        ('海外培训机构', '海外培训机构'),
    )
    xueli_leibie_choice=(
        ('合作办学双学历课程', '合作办学双学历课程'),
        ('国内本科课程', '国内本科课程'),
        ('国内专科/高职课程', '国内专科/高职课程'),
        ('国外大学预备课程', '国外大学预备课程'),
        ('国外大学学分转化课程', '国外大学学分转化课程'),
        ('国外本科课程', '国外本科课程'),
        ('国外高校副学士/Diploma课程', '国外高校副学士/Diploma课程'),
    )
    area_choice=(
        ('工程与技术', (
            ('电子电气工程', '电子电气工程'),
            ('化学工程', '化学工程'),
            ('机械，航空及制造工程', '机械，航空及制造工程'),
            ('计算机科学与信息系统', '计算机科学与信息系统'),
            ('矿物与采矿工程', '矿物与采矿工程'),
            ('土木工程与结构工程', '土木工程与结构工程'),
        )
         ),
        ('人文科学与艺术', (
            ('艺术设计', '艺术设计'),
            ('表演艺术', '表演艺术'),
            ('建筑', '建筑'),
            ('考古学', '考古学'),
            ('历史', '历史'),
            ('人类学', '人类学'),
            ('英语语言文学', '英语语言文学'),
            ('语言学', '语言学'),
            ('哲学', '哲学'),
        )
         ),
        ('社会科学与管理', (
            ('传播与媒体研究', '传播与媒体研究'),
            ('发展研究', '发展研究'),
            ('法学', '法学'),
            ('会计与金融', '会计与金融'),
            ('教育学', '教育学'),
            ('经济学与计量经济学', '经济学与计量经济学'),
            ('酒店与休闲管理', '酒店与休闲管理'),
            ('商务与管理研究', '商务与管理研究'),
            ('社会学', '社会学'),
            ('社会政策与管理', '社会政策与管理'),
            ('体育相关学科', '体育相关学科'),
            ('统计学与运营', '统计学与运营'),
            ('政治学与国际研究', '政治学与国际研究'),
        )
         ),
        ('生物科学与医学', (
            ('护理', '护理'),
            ('解剖生理学', '解剖生理学'),
            ('农林', '农林'),
            ('生物科学', '生物科学'),
            ('兽医', '兽医'),
            ('心理学', '心理学'),
            ('牙医', '牙医'),
            ('医学', '医学'),
        )
         ),
        ('自然科学', (
            ('材料科学', '材料科学'),
            ('地理学', '地理学'),
            ('地球与海洋科学', '地球与海洋科学'),
            ('化学', '化学'),
            ('环境科学', '环境科学'),
            ('数学', '数学'),
            ('物理学与天文学', '物理学与天文学'),
        )
         ),
    )
    guojia = models.CharField("国家", max_length=20, default="美国")
    liuxue_leixing = models.CharField("留学项目申请", max_length=50, choices=liuxue_leixing_choice, default='国内本科申请国外研究生/硕士课程')
    zhongwen = models.CharField("录取学校（中文）", max_length=200)
    xuezhi = models.IntegerField("学制", blank=True, null=True, default=2)
    jiangxuejin = models.IntegerField("奖学金", blank=True, null=True)
    zhuanye = models.CharField("录取专业", max_length=100)
    area = models.CharField("专业类型", max_length=100, choices=area_choice)
    chengshi = models.CharField("学员城市", max_length=50, blank=True, null=True)
    xuexiaoleibie = models.CharField("学员学校类别", max_length=50, choices=xuexiao_leibie_choice, default='重点高校（211，985，一本高校）')
    xueli = models.CharField("申请学历", max_length=50, default="硕士")
    xueli_leibie = models.CharField("就读学历类别", max_length=50, choices=xueli_leibie_choice, default='国内本科课程')
    zhuanye_ch = models.CharField("就读专业", max_length=100)
    jigou = models.CharField("代理机构", max_length=50)
    jigou_city = models.CharField("代理城市", max_length=50, default="北京")
    guwen_name = models.CharField("顾问姓名", max_length=50, blank=True, null=True,)
    anli_tese = models.CharField("案例特色", max_length=1000, blank=True, null=True,)
    gpa = models.FloatField()
    url = models.URLField(blank=True, null=True)
    offer_huoqu = models.CharField("Offer获取时间", max_length=20, blank=True, null=True, default="2016年3月")
    xuexiao = models.CharField("学员学校", max_length=50, blank=True, null=True)
    xueli_chengdu = models.CharField("就读学历程度", max_length=50, blank=True, null=True, default="12年级完成")
    ielts = models.FloatField(blank=True, null=True)
    tofel = models.IntegerField(blank=True, null=True)
    gre = models.IntegerField(blank=True, null=True)
    gmat = models.IntegerField(blank=True, null=True)
    tiaojian = models.CharField("录取条件", max_length=50, blank=True, null=True, default="Full Offer")
    p = models.IntegerField("发布", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shuoshi'
        verbose_name = '硕士Offer'
        verbose_name_plural = '硕士Offers'