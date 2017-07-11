# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-11 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCommentTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_c_time', models.CharField(blank=True, max_length=32, null=True, verbose_name='产品评论日期')),
            ],
            options={
                'db_table': 'product_comment_time',
                'verbose_name_plural': '评论日期',
            },
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_url', models.CharField(max_length=256, verbose_name='产品url')),
                ('p_title', models.CharField(max_length=32, verbose_name='产品名称')),
                ('p_img', models.CharField(max_length=256, verbose_name='产品图片')),
                ('p_price_in_jd', models.CharField(max_length=32, verbose_name='京东')),
                ('p_price_in_tmall', models.CharField(max_length=32, verbose_name='天猫')),
                ('p_price_in_zol', models.CharField(max_length=32, verbose_name='zol')),
                ('p_c_score', models.FloatField(blank=True, null=True, verbose_name='产品总评分')),
                ('p_c_good_nums', models.IntegerField(blank=True, null=True, verbose_name='产品好评数')),
                ('p_c_mid_nums', models.IntegerField(blank=True, null=True, verbose_name='产品中评数')),
                ('p_c_bad_nums', models.IntegerField(blank=True, null=True, verbose_name='产品差评数')),
                ('p_c_all_nums', models.CharField(blank=True, max_length=256, null=True, verbose_name='概况点评内容')),
            ],
            options={
                'db_table': 'product_info',
                'verbose_name_plural': '产品信息',
            },
        ),
        migrations.AddField(
            model_name='productcommenttime',
            name='p_info_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ProductInfo', verbose_name='所属产品'),
        ),
    ]
