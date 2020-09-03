import gc
import json
import re
import jieba.posseg as poss
import cpca
import os
import django
django.setup()
from .models import category, noise_judge, event
from django.db import connection
import jieba
from natural_disasters.business_models.typhoon.noise_judge.predict import Predictor as typhoon_noise_model
from natural_disasters.business_models.earthquake.noise_judge.predict import Predictor as earthquake_noise_model
from natural_disasters.business_models.rainstorm.noise_judge.predict import Predictor as rainstorm_noise_model
from celery import task
import tensorflow as tf
from django.db.models import Q
# 微博
earthquake_id = ['\'1_1\'']
rainstorm_id = ['\'1_2\'']
typhoon_id = ['\'1_3\'']
# 新浪新闻
earthquake_id1 = ['\'2_1\'']
rainstorm_id1 = ['\'2_2\'']
typhoon_id1 = ['\'2_3\'']
# 垃圾判断代码
@task
def earthquake_noise():
    cursor = connection.cursor()
    print('earthquake_noise begin')
    task_name = 'earthquake'
    task_cate = 'noise_judge'
    sql = f"select post_id,task_id,post_content from weibo_post where (task_id={'or task_id='.join(earthquake_id)}) and CONCAT(task_id,'_',post_id) not in (select CONCAT(task_id,'_',post_id) from noise_judge);"
    cursor.execute(sql)
    text = cursor.fetchall()
    noise_judges = []
    # with open(
    #         os.path.join(os.path.dirname(__file__),
    #                      f"business_models/{task_name}/{task_cate}/config/textcnn_config.json")) as f:
    #     config = json.load(f)
    # tf.reset_default_graph()
    # predictor = earthquake_noise_model(config)
    for content in text:
        if '瞳孔地震' in content[2] or '和地震一样' in content[2] or '像地震' in content[2] or '洛杉矶银河' in content[2] or '跟地震一样' in \
                content[2] or '跟地震似的' in content[2] or '梦到地震' in content[2] or '祭' in content[2] or '免费围观' in content[
            2] or '地震局' in content[2] or '地震科普' in content[2] or '转发微博' in content[2] or '地震演练' in content[
            2] or '转发微博' in content[2] or "美职足" in content[2] or "世界杯" in content[2] or "财经" in content[
            2] or "每日足球推荐" in content[2] or "体育" in content[2] or "电影" in content[2]:
            t = noise_judge(post_id=content[0], task_id=content[1], noise='1')
            noise_judges.append(t)
        else:
            # result = predictor.predict([item for item in jieba.cut(content[2], cut_all=False)])
            # if int(result) == 1:
            #     t = noise_judge(post_id=content[0], task_id=content[1], noise='0')
            #     noise_judges.append(t)
            # else:
            #     t = noise_judge(post_id=content[0], task_id=content[1], noise='1')
            #     noise_judges.append(t)
            t = noise_judge(post_id=content[0], task_id=content[1], noise='0')
            noise_judges.append(t)
    noise_judge.objects.bulk_create(noise_judges)
    cursor.close()
    gc.collect()
    print("earthquake_noise end")
@task
def earthquake_noise1():
    cursor = connection.cursor()
    print('earthquake_noise begin')
    sql = f"select post_id,task_id,title from xinlang_new where (task_id={'or task_id='.join(earthquake_id1)}) and CONCAT(task_id,'_',post_id) not in (select CONCAT(task_id,'_',post_id) from noise_judge);"
    cursor.execute(sql)
    text = cursor.fetchall()
    noise_judges = []
    for content in text:
        if '瞳孔地震' in content[2] or '和地震一样' in content[2] or '像地震' in content[2] or '洛杉矶银河' in content[2] or '跟地震一样' in \
                content[2] or '跟地震似的' in content[2] or '梦到地震' in content[2] or '祭' in content[2] or '免费围观' in content[
            2] or '地震局' in content[2] or '地震科普' in content[2] or '转发微博' in content[2] or '地震演练' in content[
            2] or '转发微博' in content[2] or "美职足" in content[2] or "世界杯" in content[2] or "财经" in content[
            2] or "每日足球推荐" in content[2] or "体育" in content[2] or "电影" in content[2]:
            t = noise_judge(post_id=content[0], task_id=content[1], noise='1')
            noise_judges.append(t)
        else:
            t = noise_judge(post_id=content[0], task_id=content[1], noise='0')
            noise_judges.append(t)
        print("success")

    noise_judge.objects.bulk_create(noise_judges)
    cursor.close()
    gc.collect()
    print("earthquake_noise end")
@task
def rainstorm_noise():
    cursor = connection.cursor()
    print('rainstorm_noise begin')
    sql = f"select post_id,task_id,post_content from weibo_post where (task_id={'or task_id='.join(rainstorm_id)}) and CONCAT(task_id,'_',post_id) not in (select CONCAT(task_id,'_',post_id) from noise_judge);"
    cursor.execute(sql)
    text = cursor.fetchall()
    noise_judges = []
    for content in text:
        try:
            if "周震南" in content[2] or '蜕变之战' in content[2] or '台团综' in content[2] or '转发微博' in content[2] or '舞台' in \
                    content[2]:
                t = noise_judge(post_id=content[0], task_id=content[1], noise='1')
                noise_judges.append(t)
            elif '红色预警' in content[2] or '黄色预警' in content[2] or '蓝色预警' in content[2]:
                t = noise_judge(post_id=content[0], task_id=content[1], noise='0')
                noise_judges.append(t)
            else:
                t = noise_judge(post_id=content[0], task_id=content[1], noise='0')
                noise_judges.append(t)
        except:
            print(content[2]);
    noise_judge.objects.bulk_create(noise_judges)
    cursor.close()
    gc.collect()
    print("rainstorm_noise end")
    return
@task
def rainstorm_noise1():
    cursor = connection.cursor()
    print('rainstorm_noise begin')
    sql = f"select post_id,task_id,title from xinlang_new where (task_id={'or task_id='.join(rainstorm_id1)}) and CONCAT(task_id,'_',post_id) not in (select CONCAT(task_id,'_',post_id) from noise_judge);"
    cursor.execute(sql)
    text = cursor.fetchall()
    noise_judges = []
    for content in text:
        try:
            if "周震南" in content[2] or '蜕变之战' in content[2] or '台团综' in content[2] or '转发微博' in content[2] or '舞台' in \
                    content[2]:
                t = noise_judge(post_id=content[0], task_id=content[1], noise='1')
                noise_judges.append(t)
            elif '红色预警' in content[2] or '黄色预警' in content[2] or '蓝色预警' in content[2]:
                t = noise_judge(post_id=content[0], task_id=content[1], noise='0')
                noise_judges.append(t)
            else:
                t = noise_judge(post_id=content[0], task_id=content[1], noise='0')
                noise_judges.append(t)
        except:
            print(content[2]);
    noise_judge.objects.bulk_create(noise_judges)
    cursor.close()
    print("rainstorm_noise end")
    return
@task
def typhoon_noise():
    cursor = connection.cursor()
    print('typhoon_noise begin')
    task_name = 'typhoon'
    task_cate = 'noise_judge'
    sql = f"select post_id,task_id,post_content from weibo_post where (task_id={'or task_id='.join(typhoon_id)}) and CONCAT(task_id,'_',post_id) not in (select CONCAT(task_id,'_',post_id) from noise_judge);"
    cursor.execute(sql)
    text = cursor.fetchall()
    noise_judges = []
    # with open(
    #         os.path.join(os.path.dirname(__file__),
    #                      f"business_models/{task_name}/{task_cate}/config/textcnn_config.json")) as f:
    #     config = json.load(f)
    # tf.reset_default_graph()
    # predictor = typhoon_noise_model(config)
    for content in text:
        try:
            if '台风' not in content[2] or "周震南" in content[2] or '蜕变之战' in content[2] or '台团综' in content[2] or '转发微博' in \
                    content[2] or '舞台' in content[2]:
                t = noise_judge(post_id=content[0], task_id=content[1], noise='1')
                noise_judges.append(t)
            else:
                # result = predictor.predict([item for item in jieba.cut(content[2], cut_all=False)])
                # if int(result) == 1:
                #     t = noise_judge(post_id=content[0], task_id=content[1], noise='0')
                #     noise_judges.append(t)
                # else:
                #     t = noise_judge(post_id=content[0], task_id=content[1], noise='1')
                #     noise_judges.append(t)
                t = noise_judge(post_id=content[0], task_id=content[1], noise='0')
                noise_judges.append(t)
        except:
            print(content[2])
    noise_judge.objects.bulk_create(noise_judges)
    cursor.close()
    print("typhoon_noise end")
    return
@task
def typhoon_noise1():
    cursor = connection.cursor()
    print('typhoon_noise begin')
    sql = f"select post_id,task_id,title from xinlang_new where (task_id={'or task_id='.join(typhoon_id1)}) and CONCAT(task_id,'_',post_id) not in (select CONCAT(task_id,'_',post_id) from noise_judge);"
    cursor.execute(sql)
    text = cursor.fetchall()
    noise_judges = []
    for content in text:
        try:
            if '台风' not in content[2] or "周震南" in content[2] or '蜕变之战' in content[2] or '台团综' in content[2] or '转发微博' in \
                    content[2] or '舞台' in content[2]:
                t = noise_judge(post_id=content[0], task_id=content[1], noise='1')
                noise_judges.append(t)
            else:
                t = noise_judge(post_id=content[0], task_id=content[1], noise='0')
                noise_judges.append(t)
        except:
            print(content[2])
    noise_judge.objects.bulk_create(noise_judges)
    cursor.close()
    gc.collect()
    print("typhoon_noise end")
    return

# 灾害造成的影响分类
@task
def earthquake_category():
    cursor = connection.cursor()
    print("earthquake_category begin")
    sql = f"select weibo_post.post_id,weibo_post.task_id,post_content from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and noise_judge.noise='0' and (noise_judge.task_id={'or noise_judge.task_id='.join(earthquake_id)}) and CONCAT(noise_judge.task_id,'_',noise_judge.post_id) not in (select CONCAT(task_id,'_',post_id) from category);"
    cursor.execute(sql)
    text = cursor.fetchall()
    categorys = []
    for content in text:
        if "房屋" in content[2] or "摧毁" in content[2] or "倒塌" in content[2]:
            t = category(task_id=content[1],post_id=content[0],category='house')
            categorys.append(t)
        elif "停运" in content[2] or "路段" in content[2] or "堵塞" in content[2]:
            t = category(task_id=content[1], post_id=content[0], category='transport')
            categorys.append(t)
        elif "死亡" in content[2] or "受伤" in content[2] or "伤亡" in content[2]:
            t = category(task_id=content[1], post_id=content[0], category='people')
            categorys.append(t)
        elif "经济损失" in content[2] or "受淹" in content[2] or "被淹" in content[2]:
            t = category(task_id=content[1], post_id=content[0], category='properties')
            categorys.append(t)
        elif "农作物" in content[2] or "农业" in content[2]:
            t = category(task_id=content[1], post_id=content[0], category='agriculture')
            categorys.append(t)
    category.objects.bulk_create(categorys)
    cursor.close()
    print("earthquake_category end")
    return
@task
def rainstorm_category():
    print("typhoon_category begin")
    cursor = connection.cursor()
    sql = f"select weibo_post.post_id,weibo_post.task_id,post_content from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and noise_judge.noise='0' and (noise_judge.task_id={'or noise_judge.task_id='.join(rainstorm_id)}) and CONCAT(noise_judge.task_id,'_',noise_judge.post_id) not in (select CONCAT(task_id,'_',post_id) from category);"
    cursor.execute(sql)
    text = cursor.fetchall()
    categorys = []
    for content in text:
        if "房屋" in content[2] or "摧毁" in content[2] or "倒塌" in content[2]:
            t = category(task_id=content[1], post_id=content[0], category='house')
            categorys.append(t)
        elif "停运" in content[2] or "路段" in content[2] or "堵塞" in content[2]:
            t = category(task_id=content[1], post_id=content[0], category='transport')
            categorys.append(t)
        elif "死亡" in content[2] or "受伤" in content[2] or "伤亡" in content[2]:
            t = category(task_id=content[1], post_id=content[0], category='people')
            categorys.append(t)
        elif "经济损失" in content[2] or "受淹" in content[2] or "被淹" in content[2]:
            t = category(task_id=content[1], post_id=content[0], category='properties')
            categorys.append(t)
        elif "农作物" in content[2] or "农业" in content[2]:
            t = category(task_id=content[1], post_id=content[0], category='agriculture')
            categorys.append(t)
    category.objects.bulk_create(categorys)
    cursor.close()
    print("rainstorm_category end")
    return
@task
def typhoon_category():
    print("typhoon_category begin")
    cursor = connection.cursor()
    sql = f"select weibo_post.post_id,weibo_post.task_id,post_content from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and noise_judge.noise='0' and (noise_judge.task_id={'or noise_judge.task_id='.join(typhoon_id)}) and CONCAT(noise_judge.task_id,'_',noise_judge.post_id) not in (select CONCAT(task_id,'_',post_id) from category);"
    cursor.execute(sql)
    text = cursor.fetchall()
    categorys = []
    for content in text:
        if "房屋" in content[2] or "摧毁" in content[2] or "倒塌" in content[2]:
            t = category(task_id=content[1], post_id=content[0], category='house')
            categorys.append(t)
        elif "停运" in content[2] or "路段" in content[2] or "堵塞" in content[2]:
            t = category(task_id=content[1], post_id=content[0], category='transport')
            categorys.append(t)
        elif "死亡" in content[2] or "受伤" in content[2] or "伤亡" in content[2]:
            t = category(task_id=content[1], post_id=content[0], category='people')
            categorys.append(t)
        elif "经济损失" in content[2] or "受淹" in content[2] or "被淹" in content[2]:
            t = category(task_id=content[1], post_id=content[0], category='properties')
            categorys.append(t)
        elif "农作物" in content[2] or "农业" in content[2]:
            t = category(task_id=content[1], post_id=content[0], category='agriculture')
            categorys.append(t)
    category.objects.bulk_create(categorys)
    cursor.close()
    print("typhoon_category end")
    return



def cut_sent(para):
    para = re.sub('([,，。！？\?])([^”’])', r"\1\n\2", para)  # 单字符断句符
    para = re.sub('(\.{6})([^”’])', r"\1\n\2", para)  # 英文省略号
    para = re.sub('(\…{2})([^”’])', r"\1\n\2", para)  # 中文省略号
    para = re.sub('([。！？\?][”’])([^，。！？\?])', r'\1\n\2', para)
    # 如果双引号前有终止符，那么双引号才是句子的终点，把分句符\n放到双引号后，注意前面的几句都小心保留了双引号
    para = para.rstrip()  # 段尾如果有多余的\n就去掉它
    # 很多规则中会考虑分号;，但是这里我把它忽略不计，破折号、英文双引号等同样忽略，需要的再做些简单调整即可。
    return para.split("\n")
# 事件抽取及命名实体识别
@task
def earthquake_event():
    print("earthquake_event begin")
    cursor = connection.cursor()
    sql = f"select weibo_post.post_id,weibo_post.task_id,post_content,post_time from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and noise_judge.noise='0' and (noise_judge.task_id={'or noise_judge.task_id='.join(earthquake_id)}) and CONCAT(noise_judge.task_id,'_',noise_judge.post_id) not in (select CONCAT(task_id,'_',post_id) from event);"
    cursor.execute(sql)
    text = cursor.fetchall()
    events = []
    for content in text:
        try:
            text = content[2]
            for i in cut_sent(text):
                values = cpca.transform([i], open_warning=False).values
                province = values[0][0]
                city = values[0][1]
                area = values[0][2]
                if(len(province) != 0):
                    break
            e = re.search("发生.{0,6}?地震", content[2])
            # print(text, province, city, area)
            if e != None:
                e = e.group(0)
            if len(province) == 0 and len(city) == 0 and len(area) == 0:
                continue
            else:
                t = event(task_id=content[1], post_id=content[0], province=province, city=city, area=area,event=e,time=content[3])
                events.append(t)
        except:
            continue
    event.objects.bulk_create(events)
    cursor.close()
    print("earthquake_event end")
    return
@task
def rainstorm_event():
    print("rainstorm_event begin")
    cursor = connection.cursor()
    sql = f"select weibo_post.post_id,weibo_post.task_id,post_content,post_time from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and noise_judge.noise='0' and (noise_judge.task_id={'or noise_judge.task_id='.join(rainstorm_id)}) and CONCAT(noise_judge.task_id,'_',noise_judge.post_id) not in (select CONCAT(task_id,'_',post_id) from event);"
    cursor.execute(sql)
    text = cursor.fetchall()
    events = []
    for content in text:
        try:
            text = content[2]
            for i in cut_sent(text):
                values = cpca.transform([i], open_warning=False).values
                province = values[0][0]
                city = values[0][1]
                area = values[0][2]
                if (len(province) != 0):
                    break
            e = re.search("强降雨", content[2])
            e1 = re.search("暴雨", content[2])
            e2 = re.search("大暴雨", content[2])
            e3 = re.search("特大暴雨", content[2])
            if e != None:
                e = "发生" + e.group(0)
            if e1 != None:
                e = "发生" + e1.group(0)
            if e2 != None:
                e = "发生" + e2.group(0)
            if e3 != None:
                e = "发生" + e3.group(0)
            if len(province) == 0 and len(city) == 0 and len(area) == 0:
                continue
            else:
                t = event(task_id=content[1], post_id=content[0], province=province, city=city, area=area, event=e,
                          time=content[3])
                events.append(t)
        except:
            continue
    event.objects.bulk_create(events)
    cursor.close()
    print("rainstorm_event end")
    return
@task
def typhoon_event():
    print("typhoon_event begin")
    cursor = connection.cursor()
    sql = f"select weibo_post.post_id,weibo_post.task_id,post_content,post_time from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and noise_judge.noise='0' and (noise_judge.task_id={'or noise_judge.task_id='.join(typhoon_id)}) and CONCAT(noise_judge.task_id,'_',noise_judge.post_id) not in (select CONCAT(task_id,'_',post_id) from event);"
    cursor.execute(sql)
    text = cursor.fetchall()
    events = []
    for content in text:
        try:
            text = content[2]
            for i in cut_sent(text):
                values = cpca.transform([i], open_warning=False).values
                province = values[0][0]
                city = values[0][1]
                area = values[0][2]
                if (len(province) != 0):
                    break
            e = re.search("台风", content[2])
            e1 = re.search("强台风", content[2])
            e2 = re.search("超强台风", content[2])
            if e != None:
                e = "发生" + e.group(0)
            if e1 != None:
                e = "发生" + e1.group(0)
            if e2 != None:
                e = "发生" + e2.group(0)
            if len(province) == 0 and len(city) == 0 and len(area) == 0:
                continue
            else:
                t = event(task_id=content[1], post_id=content[0], province=province, city=city, area=area, event=e,
                          time=content[3])
                events.append(t)
        except:
            continue
    event.objects.bulk_create(events)
    cursor.close()
    print("typhoon_event end")
    return


@task
def earthquake_cluster():
    print("earthquake_cluster begin")
    cursor = connection.cursor()
    sql = f"select post_id,task_id,province,time from event where (task_id={'or task_id='.join(earthquake_id)}) order by province,time;"
    cursor.execute(sql)
    data = cursor.fetchall()
    cluster = 1
    province = None
    event_time = None
    for content in data:
        if(province == None and event_time == None):
            province = content[2]
            event_time = content[3]
        else:
            if province != content[2] or abs((content[3]-event_time).days)>30:
                province = content[2]
                event_time = content[3]
                cluster = cluster + 1
        event.objects.filter(Q(task_id=content[1])&Q(post_id=content[0])).update(cluster=str(cluster))
    cursor.close()
    print("earthquake_cluster end")
    return
@task
def typhoon_cluster():
    print("typhoon_cluster begin")
    cursor = connection.cursor()
    sql = f"select post_id,task_id,province,time from event where (task_id={'or task_id='.join(typhoon_id)}) order by province,time;"
    cursor.execute(sql)
    data = cursor.fetchall()
    cluster = 1
    province = None
    event_time = None
    for content in data:
        if (province == None and event_time == None):
            province = content[2]
            event_time = content[3]
        else:
            if province != content[2] or abs((content[3] - event_time).days) > 15:
                province = content[2]
                event_time = content[3]
                cluster = cluster + 1
        event.objects.filter(Q(task_id=content[1]) & Q(post_id=content[0])).update(cluster=str(cluster))
    cursor.close()
    print("typhoon_cluster end")
    return
@task
def rainstorm_cluster():
    print("rainstorm_cluster begin")
    cursor = connection.cursor()
    sql = f"select post_id,task_id,province,time from event where (task_id={'or task_id='.join(rainstorm_id)}) order by province,time;"
    cursor.execute(sql)
    data = cursor.fetchall()
    cluster = 1
    province = None
    event_time = None
    for content in data:
        if (province == None and event_time == None):
            province = content[2]
            event_time = content[3]
        else:
            if province != content[2] or abs((content[3] - event_time).days) > 8:
                province = content[2]
                event_time = content[3]
                cluster = cluster + 1
        event.objects.filter(Q(task_id=content[1]) & Q(post_id=content[0])).update(cluster=str(cluster))
    cursor.close()
    print("rainstorm_cluster end")
    return