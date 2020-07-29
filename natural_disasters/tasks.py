import json
import os
import django
django.setup()
from .models import category, noise_judge
from django.db import connection
# import jieba
# from natural_disasters.business_models.typhoon.noise_judge.predict import Predictor as typhoon_noise_model
# from natural_disasters.business_models.earthquake.noise_judge.predict import Predictor as earthquake_noise_model
# from natural_disasters.business_models.rainstorm.noise_judge.predict import Predictor as rainstorm_noise_model
from celery import task
import random
# 垃圾判断代码
@task
def earthquake_noise():
    cursor = connection.cursor()
    print('earthquake')
    earthquake_id = ['\'1_1\'']
    task_name = 'earthquake'
    task_cate = 'noise_judge'
    sql = f"select post_id,task_id,post_content from weibo_post where (task_id={'or task_id='.join(earthquake_id)}) and CONCAT_WS(task_id,'_',post_id) not in (select CONCAT_WS(task_id,'_',post_id) from noise_judge);"
    cursor.execute(sql)
    text = cursor.fetchall()
    noise_judges = []
    # with open(
    #         os.path.join(os.path.dirname(__file__),
    #                      f"business_models\\{task_name}\\{task_cate}\\config\\textcnn_config.json")) as f:
    #     config = json.load(f)
    # predictor = earthquake_noise_model(config)
    for content in text:
        t = noise_judge(post_id=content[0], task_id=content[1], noise=random.choice(['0', '1']))
        noise_judges.append(t)
        # if '瞳孔地震' in content[2] or '和地震一样' in content[2] or '像地震' in content[2] or '洛杉矶银河' in content[2] or '跟地震一样' in \
        #         content[2] or '跟地震似的' in content[2] or '梦到地震' in content[2] or '祭' in content[2] or '免费围观' in content[
        #     2] or '地震局' in content[2] or '地震科普' in content[2] or '转发微博' in content[2] or '地震演练' in content[
        #     2] or '转发微博' in content[2] or "美职足" in content[2] or "世界杯" in content[2] or "财经" in content[
        #     2] or "每日足球推荐" in content[2] or "体育" in content[2] or "电影" in content[2]:
        #     t = noise_judge(post_id=content[0], task_id=content[1], noise='1')
        #     noise_judges.append(t)
        # else:
        #     result = predictor.predict([item for item in jieba.cut(content[2], cut_all=False)])
        #     if int(result) == 1:
        #         t = noise_judge(post_id=content[0], task_id=content[1], noise='0')
        #         noise_judges.append(t)
        #     else:
        #         t = noise_judge(post_id=content[0], task_id=content[1], noise='1')
        #         noise_judges.append(t)
    noise_judge.objects.bulk_create(noise_judges)
    return
@task
def typhoon_noise():
    cursor = connection.cursor()
    print('typhoon')
    typhoon_id = ['\'1_2\'']
    task_name = 'typhoon'
    task_cate = 'noise_judge'
    sql = f"select post_id,task_id,post_content from weibo_post where (task_id={'or task_id='.join(typhoon_id)}) and CONCAT_WS(task_id,'_',post_id) not in (select CONCAT_WS(task_id,'_',post_id) from noise_judge);"
    cursor.execute(sql)
    text = cursor.fetchall()
    noise_judges = []
    # with open(
    #         os.path.join(os.path.dirname(__file__),
    #                      f"business_models\\{task_name}\\{task_cate}\\config\\textcnn_config.json")) as f:
    #     config = json.load(f)
    # predictor = typhoon_noise_model(config)
    for content in text:
        t = noise_judge(post_id=content[0], task_id=content[1], noise=random.choice(['0', '1']))
        noise_judges.append(t)
        # try:
        #     if '台风' not in content[2] or "周震南" in content[2] or '蜕变之战' in content[2] or '台团综' in content[2] or '转发微博' in \
        #             content[2] or '舞台' in content[2]:
        #         t = noise_judge(post_id=content[0], task_id=content[1], noise='1')
        #         noise_judges.append(t)
        #     else:
        #         result = predictor.predict([item for item in jieba.cut(content[2], cut_all=False)])
        #         if int(result) == 1:
        #             t = noise_judge(post_id=content[0], task_id=content[1], noise='0')
        #             noise_judges.append(t)
        #         else:
        #             t = noise_judge(post_id=content[0], task_id=content[1], noise='1')
        #             noise_judges.append(t)
        # except:
        #     print(content[2])
    noise_judge.objects.bulk_create(noise_judges)
    return
@task
def rainstorm_noise():
    cursor = connection.cursor()
    print('rainstorm')
    rainstorm_id = ['\'1_3\'']
    task_name = 'rainstorm'
    task_cate = 'noise_judge'
    sql = f"select post_id,task_id,post_content from weibo_post where (task_id={'or task_id='.join(rainstorm_id)}) and CONCAT_WS(task_id,'_',post_id) not in (select CONCAT_WS(task_id,'_',post_id) from noise_judge);"
    cursor.execute(sql)
    text = cursor.fetchall()
    noise_judges = []
    # with open(
    #         os.path.join(os.path.dirname(__file__),
    #                      f"business_models\\{task_name}\\{task_cate}\\config\\textcnn_config.json")) as f:
    #     config = json.load(f)
    # predictor = rainstorm_noise_model(config)
    for content in text:
        t = noise_judge(post_id=content[0], task_id=content[1], noise=random.choice(['0', '1']))
        noise_judges.append(t)
        # try:
        #     if "周震南" in content[2] or '蜕变之战' in content[2] or '台团综' in content[2] or '转发微博' in content[2] or '舞台' in \
        #             content[2]:
        #         t = noise_judge(post_id=content[0], task_id=content[1], noise='1')
        #         noise_judges.append(t)
        #     elif '红色预警' in content[2] or '黄色预警' in content[2] or '蓝色预警' in content[2]:
        #         t = noise_judge(post_id=content[0], task_id=content[1], noise='0')
        #         noise_judges.append(t)
        #     else:
        #         result = predictor.predict([item for item in jieba.cut(content[2], cut_all=False)])
        #         if int(result) == 1:
        #             t = noise_judge(post_id=content[0], task_id=content[1], noise='0')
        #             noise_judges.append(t)
        #         else:
        #             t = noise_judge(post_id=content[0], task_id=content[1], noise='1')
        #             noise_judges.append(t)
        # except:
        #     print(content[2]);
    noise_judge.objects.bulk_create(noise_judges)
    return


# 灾害造成的影响分类
# def earthquake_category():
#     task_id = '1_1'
#     sql = f"select weibo_post.post_id,weibo_post.task_id,post_content from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and noise_judge.noise='0' and noise_judge.task_id=\'{task_id}\';"
#     cursor.execute(sql)
#     text = cursor.fetchall()
#     categorys = []
#     for content in text:
#         if "房屋倒塌" in content[2] or "房屋摧毁" in content[2]:
#             t = category(task_id=task_id,post_id=content[0],category='house')
#             categorys.append(t)
#         if "停运" in content[2]:
#             t = category(task_id=task_id, post_id=content[0], category='transport')
#             categorys.append(t)
#         if "死亡" in content[2] or "受伤" in content[2]:
#             t = category(task_id=task_id, post_id=content[0], category='people')
#             categorys.append(t)
#         if "经济损失" in content[2] or "受淹" in content[2] or "被淹" in content[2]:
#             t = category(task_id=task_id, post_id=content[0], category='properties')
#             categorys.append(t)
#         if "农作物" in content[2] or "农业" in content[2]:
#             t = category(task_id=task_id, post_id=content[0], category='agriculture')
#             categorys.append(t)
#     for i in categorys:
#         try:
#             i.save()
#         except:
#             print(i)
#     #category.objects.bulk_create(categorys)
#     return
# def typhoon_category():
#     task_id = '1_2'
#     sql = f"select weibo_post.post_id,weibo_post.task_id,post_content from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and noise_judge.noise='0' and noise_judge.task_id=\'{task_id}\';"
#     cursor.execute(sql)
#     text = cursor.fetchall()
#     categorys = []
#     for content in text:
#         if "房屋倒塌" in content[2] or "房屋摧毁" in content[2]:
#             t = category(task_id=task_id,post_id=content[0],category='house')
#             categorys.append(t)
#         if "停运" in content[2]:
#             t = category(task_id=task_id, post_id=content[0], category='transport')
#             categorys.append(t)
#         if "死亡" in content[2] or "受伤" in content[2]:
#             t = category(task_id=task_id, post_id=content[0], category='people')
#             categorys.append(t)
#         if "经济损失" in content[2] or "受淹" in content[2] or "被淹" in content[2]:
#             t = category(task_id=task_id, post_id=content[0], category='properties')
#             categorys.append(t)
#         if "农作物" in content[2] or "农业" in content[2]:
#             t = category(task_id=task_id, post_id=content[0], category='agriculture')
#             categorys.append(t)
#     for i in categorys:
#         try:
#             i.save()
#         except:
#             print(i)
#     #category.objects.bulk_create(categorys)
#     return
# def rainstorm_category():
#     task_id = '1_3'
#     sql = f"select weibo_post.post_id,weibo_post.task_id,post_content from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and noise_judge.noise='0' and noise_judge.task_id=\'{task_id}\';"
#     cursor.execute(sql)
#     text = cursor.fetchall()
#     categorys = []
#     for content in text:
#         if "房屋倒塌" in content[2] or "房屋摧毁" in content[2]:
#             t = category(task_id=task_id,post_id=content[0],category='house')
#             categorys.append(t)
#         if "停运" in content[2]:
#             t = category(task_id=task_id, post_id=content[0], category='transport')
#             categorys.append(t)
#         if "死亡" in content[2] or "受伤" in content[2]:
#             t = category(task_id=task_id, post_id=content[0], category='people')
#             categorys.append(t)
#         if "经济损失" in content[2] or "受淹" in content[2] or "被淹" in content[2]:
#             t = category(task_id=task_id, post_id=content[0], category='properties')
#             categorys.append(t)
#         if "农作物" in content[2] or "农业" in content[2]:
#             t = category(task_id=task_id, post_id=content[0], category='agriculture')
#             categorys.append(t)
#     #category.objects.bulk_create(categorys)
#     for i in categorys:
#         try:
#             i.save()
#         except:
#             print(i)
#     return

# 事件抽取及命名实体识别