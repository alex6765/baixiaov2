from django.contrib import admin
from .models import Benke, Shuoshi


class BenkeAdmin(admin.ModelAdmin):
    list_display = ('id', 'zhongwen', 'jigou', 'gpa', 'tofel', 'ielts', 'sat', 'act')
    fieldsets = [
        ('学校信息', {'fields':['liuxue_leixing', 'offer_huoqu', 'tiaojian', 'guojia', 'zhongwen', 'xueli', 'xuezhi', 'jiangxuejin', 'zhuanye', 'area']}),
        ('代理信息', {'fields':['jigou', 'jigou_city', 'guwen_name', 'url', 'anli_tese' ]}),
        ('学员信息', {'fields':['chengshi', 'xuexiao', 'xuexiaoleibie', 'xueli_leibie', 'xueli_chengdu', 'gaokao',
                            'gpa', 'ielts', 'tofel', 'sat', 'act']}),
    ]
    list_filter = ('guojia', 'zhuanye', 'xuezhi', 'jigou', 'chengshi', 'xuexiaoleibie', 'xueli_leibie', 'xueli_chengdu')

admin.site.register(Benke, BenkeAdmin)


class ShuoshiAdmin(admin.ModelAdmin):
    list_display = ('id', 'zhongwen', 'jigou', 'gpa', 'tofel', 'ielts', 'gre', 'gmat')
    fieldsets = [
        ('学校信息', {'fields':['liuxue_leixing', 'offer_huoqu', 'tiaojian', 'guojia', 'zhongwen', 'xueli', 'xuezhi', 'jiangxuejin', 'zhuanye', 'area']}),
        ('代理信息', {'fields':['jigou', 'jigou_city','guwen_name',  'url', 'anli_tese']}),
        ('学员信息', {'fields':['chengshi', 'zhuanye_ch', 'xuexiao', 'xuexiaoleibie', 'xueli_leibie', 'xueli_chengdu',
                            'gpa', 'ielts', 'tofel', 'gre', 'gmat']}),
    ]
    list_filter = ('guojia', 'zhuanye', 'zhuanye_ch', 'xuezhi', 'jigou', 'chengshi', 'xuexiaoleibie', 'xueli_leibie', 'xueli_chengdu')


admin.site.register(Shuoshi, ShuoshiAdmin)