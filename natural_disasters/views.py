import os
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

#from .tasks import earthquake_noise, typhoon_noise, rainstorm_noise, earthquake_event, typhoon_event, rainstorm_event, \
#    earthquake_category, rainstorm_category, typhoon_category, earthquake_cluster, typhoon_cluster, rainstorm_cluster
from .tasks import earthquake_noise1,rainstorm_noise1,typhoon_noise1

# 微博
earthquake_id = ['\'1_1\'']
rainstorm_id = ['\'1_2\'']
typhoon_id = ['\'1_3\'']
# 新浪新闻
earthquake_id1 = ['\'2_1\'']
rainstorm_id1 = ['\'2_2\'']
typhoon_id1 = ['\'2_3\'']

from django.shortcuts import render
from .models import weibo_post, noise_judge, category, event, xinlang_new
import json
import random
from django.db import connection
import collections
def home(request):
    rainstorm_noise1()
    cursor = connection.cursor()
    # 统计每个月灾害文章数量
    sql1 = f"select DATE_FORMAT(post_time,'%Y-%m'),count(*) from weibo_post,noise_judge where noise='0' and (noise_judge.task_id={'or noise_judge.task_id='.join(earthquake_id)}) and weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id group by DATE_FORMAT(post_time,'%Y-%m');"
    sql2 = f"select DATE_FORMAT(post_time,'%Y-%m'),count(*) from weibo_post,noise_judge where noise='0' and (noise_judge.task_id={'or noise_judge.task_id='.join(typhoon_id)}) and weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id group by DATE_FORMAT(post_time,'%Y-%m');"
    sql3 = f"select DATE_FORMAT(post_time,'%Y-%m'),count(*) from weibo_post,noise_judge where noise='0' and (noise_judge.task_id={'or noise_judge.task_id='.join(rainstorm_id)}) and weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id group by DATE_FORMAT(post_time,'%Y-%m');"
    cursor.execute(sql1)
    ret1 = cursor.fetchall()
    cursor.execute(sql2)
    ret2 = cursor.fetchall()
    cursor.execute(sql3)
    ret3 = cursor.fetchall()
    #统计每个月的灾害数
    data = {}
    for row in ret1:
        if str(row[0]) not in data:
            data[str(row[0])] = [int(row[1]),0,0]
        else:
            data[str(row[0])][0] = int(row[1])
    for row in ret2:
        if str(row[0]) not in data:
            data[str(row[0])] = [0,int(row[1]),0]
        else:
            data[str(row[0])][1] = int(row[1])
    for row in ret3:
        if str(row[0]) not in data:
            data[str(row[0])] = [0,0,int(row[1])]
        else:
            data[str(row[0])][2] = int(row[1])
    data1 = []
    for k,v in data.items():
        data1.append({
            'y':k,
            'a':v[0],
            'b':v[1],
            'c':v[2]
        })
# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    #统计每种类型灾害总数
    sql1 = f"select count(*) from noise_judge where noise='0' and (task_id={'or task_id='.join(earthquake_id)});"
    sql2 = f"select count(*) from noise_judge where noise='0' and (task_id={'or task_id='.join(typhoon_id)});"
    sql3 = f"select count(*) from noise_judge where noise='0' and (task_id={'or task_id='.join(rainstorm_id)});"
    cursor.execute(sql1)
    ret1 = cursor.fetchall()
    cursor.execute(sql2)
    ret2 = cursor.fetchall()
    cursor.execute(sql3)
    ret3 = cursor.fetchall()

    data2 = []
    count = []
    a = int(ret1[0][0])
    count.append(a)
    data2.append({'label': '地震', 'value': a})

    a = int(ret2[0][0])
    count.append(a)
    data2.append({'label': '台风', 'value': a})

    a = int(ret3[0][0])
    count.append(a)
    data2.append({'label': '暴雨', 'value': a})
    context = {
			'datajson':json.dumps(data1),
            'datajson2':json.dumps(data2),
    }
    cursor.close()
    return render(request, 'home.html',context)
def history(request):
    cursor = connection.cursor()
    type = request.GET['type']
    relevant = request.GET['relevant']
    page_now = abs(int(request.GET.get('page',-1)))
    if type == '0' and relevant == '0':
        sql = f"select weibo_post.post_id,noise,post_time,post_content from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id order by post_time DESC;"
    elif type == '1' and relevant == '0':
        sql = f"select weibo_post.post_id,noise,post_time,post_content from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and (noise_judge.task_id={'or noise_judge.task_id='.join(earthquake_id)}) order by post_time DESC;"
    elif type == '2' and relevant == '0':
        sql = f"select weibo_post.post_id,noise,post_time,post_content from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and (noise_judge.task_id={'or noise_judge.task_id='.join(typhoon_id)}) order by post_time DESC;"
    elif type == '3' and relevant == '0':
        sql = f"select weibo_post.post_id,noise,post_time,post_content from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and (noise_judge.task_id={'or noise_judge.task_id='.join(rainstorm_id)}) order by post_time DESC;"

    elif type == '0' and relevant == '1':
        sql = f"select weibo_post.post_id,noise,post_time,post_content from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and noise='0' order by post_time DESC;"
    elif type == '1' and relevant == '1':
        sql = f"select weibo_post.post_id,noise,post_time,post_content from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and (noise_judge.task_id={'or noise_judge.task_id='.join(earthquake_id)}) and noise='0' order by post_time DESC;"
    elif type == '2' and relevant == '1':
        sql = f"select weibo_post.post_id,noise,post_time,post_content from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and (noise_judge.task_id={'or noise_judge.task_id='.join(typhoon_id)}) and noise='0' order by post_time DESC;"
    elif type == '3' and relevant == '1':
        sql = f"select weibo_post.post_id,noise,post_time,post_content from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and (noise_judge.task_id={'or noise_judge.task_id='.join(rainstorm_id)}) and noise='0' order by post_time DESC;"
    cursor.execute(sql)
    ret = cursor.fetchall()
    page_list = []
    for row in ret:
        record = {
                'isnoise': "相关" if str(row[1])=='0' else "不相关",
                'weibo_id': row[0],
                'original_text':row[3],
                'time': str(row[2])[:10]
            }
        page_list.append(record)
    paginator = Paginator(page_list,20)

    if paginator.num_pages > 7:
        if page_now - 3 < 1:
            page_range = range(1, 7)
        elif page_now + 3 > paginator.num_pages:
            page_range = range(paginator.num_pages - 6, paginator.num_pages + 1)
        else:
            page_range = range(page_now - 3, page_now + 4)
    else:
        page_range = paginator.page_range
    try:
        page = paginator.page(page_now)
    except EmptyPage as e:
        # 如果出现的是负数，或者大于页码的数，我们默认让其显示第一页
        page = paginator.page(1)

    return render(request, 'history.html', {"page":page,"page_range":page_range})
def history1(request):
    cursor = connection.cursor()
    type = request.GET['type']
    relevant = request.GET['relevant']
    page_now = abs(int(request.GET.get('page',-1)))
    if type == '0' and relevant == '0':
        xinlang_new.objects.filter()
        sql = f"select xinlang_new.post_id,noise,date,title from xinlang_new,noise_judge where xinlang_new.post_id=noise_judge.post_id and xinlang_new.task_id=noise_judge.task_id order by date DESC limit 1000;"
    elif type == '1' and relevant == '0':
        sql = f"select xinlang_new.post_id,noise,date,title from xinlang_new,noise_judge where xinlang_new.post_id=noise_judge.post_id and xinlang_new.task_id=noise_judge.task_id and (noise_judge.task_id={'or noise_judge.task_id='.join(earthquake_id1)}) order by date DESC;"
    elif type == '2' and relevant == '0':
        sql = f"select xinlang_new.post_id,noise,date,title from xinlang_new,noise_judge where xinlang_new.post_id=noise_judge.post_id and xinlang_new.task_id=noise_judge.task_id and (noise_judge.task_id={'or noise_judge.task_id='.join(typhoon_id1)}) order by date DESC;"
    elif type == '3' and relevant == '0':
        sql = f"select xinlang_new.post_id,noise,date,title from xinlang_new,noise_judge where xinlang_new.post_id=noise_judge.post_id and xinlang_new.task_id=noise_judge.task_id and (noise_judge.task_id={'or noise_judge.task_id='.join(rainstorm_id1)}) order by date DESC;"

    elif type == '0' and relevant == '1':
        sql = f"select xinlang_new.post_id,noise,date,title from xinlang_new,noise_judge where xinlang_new.post_id=noise_judge.post_id and xinlang_new.task_id=noise_judge.task_id and noise='0' order by date DESC limit 1000;"
    elif type == '1' and relevant == '1':
        sql = f"select xinlang_new.post_id,noise,date,title from xinlang_new,noise_judge where xinlang_new.post_id=noise_judge.post_id and xinlang_new.task_id=noise_judge.task_id and (noise_judge.task_id={'or noise_judge.task_id='.join(earthquake_id1)}) and noise='0' order by date DESC;"
    elif type == '2' and relevant == '1':
        sql = f"select xinlang_new.post_id,noise,date,title from xinlang_new,noise_judge where xinlang_new.post_id=noise_judge.post_id and xinlang_new.task_id=noise_judge.task_id and (noise_judge.task_id={'or noise_judge.task_id='.join(typhoon_id1)}) and noise='0' order by date DESC;"
    elif type == '3' and relevant == '1':
        sql = f"select xinlang_new.post_id,noise,date,title from xinlang_new,noise_judge where xinlang_new.post_id=noise_judge.post_id and xinlang_new.task_id=noise_judge.task_id and (noise_judge.task_id={'or noise_judge.task_id='.join(rainstorm_id1)}) and noise='0' order by date DESC;"
    cursor.execute(sql)
    ret = cursor.fetchall()
    page_list = []
    for row in ret:
        record = {
                'isnoise': "相关" if str(row[1])=='0' else "不相关",
                'weibo_id': row[0],
                'original_text':row[3],
                'time': str(row[2])[:10]
            }
        page_list.append(record)
    paginator = Paginator(page_list,20)
    if paginator.num_pages > 7:
        if page_now - 3 < 1:
            page_range = range(1, 7)
        elif page_now + 3 > paginator.num_pages:
            page_range = range(paginator.num_pages - 6, paginator.num_pages + 1)
        else:
            page_range = range(page_now - 3, page_now + 4)
    else:
        page_range = paginator.page_range
    try:
        page = paginator.page(page_now)
    except EmptyPage as e:
        # 如果出现的是负数，或者大于页码的数，我们默认让其显示第一页
        page = paginator.page(1)

    return render(request, 'history1.html', {"page":page,"page_range":page_range})
def detail(request):
    id = request.GET['id']
    row = weibo_post.objects.filter(post_id=id).first()
    context = {
        'weibo_id': row.post_id,
        'user_id': row.user_id,
        'time': row.post_time,
        'text': row.post_content
    }
    return render(request, 'detail.html', context)
def detail1(request):
    id = request.GET['id']
    row = xinlang_new.objects.filter(post_id=id).first()
    context = {
        'weibo_id': row.post_id,
        'title': row.title,
        'time': row.date,
        'text': row.content
    }
    return render(request, 'detail1.html', context)
def detail_all(request):
    cursor = connection.cursor()
    task_id = str(request.GET['task_id'])
    task_id = task_id.split('-')
    tmp = []
    for i in task_id:
        tmp.append("'"+i+"'")
    task_id = tmp
    province = str(request.GET['province'])
    cluster = str(request.GET['cluster'])
    sql = f"select weibo_post.post_id,weibo_post.user_id,weibo_post.post_time,weibo_post.post_content from `event` e,weibo_post where weibo_post.post_id=e.post_id and weibo_post.task_id=e.task_id and (weibo_post.task_id={'or weibo_post.task_id='.join(task_id)}) and province like '%{province}%' and cluster='{cluster}' order by post_time;"
    cursor.execute(sql);
    res = cursor.fetchall()
    data = []
    for row in res:
        tmp = {
            'weibo_id': str(row[0]),
            'user_id': str(row[1]),
            'time': str(row[2]),
            'text': str(row[3])
        }
        data.append(tmp)
    context = {
        'datas':data
    }
    return render(request, 'detail_all.html', context)
def statistical(request):
    cursor = connection.cursor()
    #地震
    sql = f"select count(*) from event where (task_id={'or task_id='.join(earthquake_id)});"
    cursor.execute(sql)
    ret = cursor.fetchall()
    count = int(ret[0][0])
    sql = f"select count(distinct province) from event where (task_id={'or task_id='.join(earthquake_id)});"
    cursor.execute(sql)
    ret = cursor.fetchall()
    num = int(ret[0][0])
    sql = f"select DATE_FORMAT(time,'%Y-%m') from event where (task_id={'or task_id='.join(earthquake_id)}) group by DATE_FORMAT(time,'%Y-%m') order by count(*) DESC limit 1;"
    cursor.execute(sql)
    ret = cursor.fetchall()
    month = str(ret[0][0])
    earthquake_brief = {
        'count': count,
        'num': num,
        'month': month,
    }
    sql = f"select count(*) ,DATE_FORMAT(time,'%Y-%m'),province from event where (task_id={'or task_id='.join(earthquake_id)}) group by DATE_FORMAT(time,'%Y-%m'),province having count(*)>1 order by count(*) DESC limit 5;"
    cursor.execute(sql)
    ret3 = cursor.fetchall()
    num = 0
    earthquake_information = []
    for row in ret3:
        num += 1
        record = {
            'num': num,
            'time': row[1],
            'location': row[2],
            'count': row[0],
        }
        earthquake_information.append(record)


    #台风
    sql = f"select count(*) from event where (task_id={'or task_id='.join(typhoon_id)});"
    cursor.execute(sql)
    ret = cursor.fetchall()
    count = int(ret[0][0])
    sql = f"select count(distinct province) from event where (task_id={'or task_id='.join(typhoon_id)});"
    cursor.execute(sql)
    ret = cursor.fetchall()
    num = int(ret[0][0])
    sql = f"select DATE_FORMAT(time,'%Y-%m') from event where (task_id={'or task_id='.join(typhoon_id)}) group by DATE_FORMAT(time,'%Y-%m') order by count(*) DESC limit 1;"
    cursor.execute(sql)
    ret = cursor.fetchall()
    month = str(ret[0][0])
    typhoon_brief = {
        'count': count,
        'num': num,
        'month': month,
    }
    sql = f"select count(*) ,DATE_FORMAT(time,'%Y-%m'),province from event where (task_id={'or task_id='.join(typhoon_id)}) group by DATE_FORMAT(time,'%Y-%m'),province having count(*)>1 order by count(*) DESC limit 5;"
    cursor.execute(sql)
    ret3 = cursor.fetchall()
    num = 0
    typhoon_information = []
    for row in ret3:
        num += 1
        record = {
            'num': num,
            'time': row[1],
            'location': row[2],
            'count': row[0],
        }
        typhoon_information.append(record)


    # 暴雨
    task_id = '1_3'
    sql = f"select count(*) from event where (task_id={'or task_id='.join(rainstorm_id)});"
    cursor.execute(sql)
    ret = cursor.fetchall()
    count = int(ret[0][0])
    sql = f"select count(distinct province) from event where (task_id={'or task_id='.join(rainstorm_id)});"
    cursor.execute(sql)
    ret = cursor.fetchall()
    num = int(ret[0][0])
    sql = f"select DATE_FORMAT(time,'%Y-%m') from event where (task_id={'or task_id='.join(rainstorm_id)}) group by DATE_FORMAT(time,'%Y-%m') order by count(*) DESC limit 1;"
    cursor.execute(sql)
    ret = cursor.fetchall()
    month = str(ret[0][0])
    rainstorm_brief = {
        'count': count,
        'num': num,
        'month': month,
    }
    sql = f"select count(*) ,DATE_FORMAT(time,'%Y-%m'),province from event where (task_id={'or task_id='.join(rainstorm_id)}) group by DATE_FORMAT(time,'%Y-%m'),province having count(*)>1 order by count(*) DESC limit 5;"
    cursor.execute(sql)
    ret3 = cursor.fetchall()
    num = 0
    rainstorm_information = []
    for row in ret3:
        num += 1
        record = {
            'num': num,
            'time': row[1],
            'location': row[2],
            'count': row[0],
        }
        rainstorm_information.append(record)






    def randomColor():
        s = '#'
        for i in range(6):
            randNum = random.randint(0, 15);
            if randNum==10:
                randNum = 'a'
            elif randNum==11:
                randNum = 'b'
            elif randNum==12:
                randNum = 'c'
            elif randNum==13:
                randNum = 'd'
            elif randNum==14:
                randNum = 'e'
            elif randNum==15:
                randNum = 'f'
            s+=str(randNum)
        return s



    #地震
    sql = f"SELECT province, count(*) from event where (task_id={'or task_id='.join(earthquake_id)}) group by province order by count(*) DESC;"
    cursor.execute(sql)
    ret3 = cursor.fetchall()
    hoverBackgroundColor = []
    data = []
    num_rows = 0
    for row in ret3:
        if int(row[1])<10:
            break
        num_rows = num_rows + 1
        hoverBackgroundColor.append(randomColor())
        data.append({
            'label': row[0],
            'value': int(row[1]),
        })
    #台风
    sql = f"SELECT province, count(*) from event where (task_id={'or task_id='.join(typhoon_id)}) group by province order by count(*) DESC;"
    cursor.execute(sql)
    ret3 = cursor.fetchall()
    hoverBackgroundColor2 = []
    data2 = []
    num_rows = 0
    for row in ret3:
        if int(row[1]) < 10:
            break
        num_rows = num_rows + 1
        hoverBackgroundColor2.append(randomColor())
        data2.append({
            'label': row[0],
            'value': int(row[1]),
        })
    #暴雨
    sql = f"SELECT province, count(*) from event where (task_id={'or task_id='.join(rainstorm_id)}) group by province order by count(*) DESC;"
    cursor.execute(sql)
    ret3 = cursor.fetchall()
    hoverBackgroundColor3 = []
    data3 = []
    num_rows = 0
    for row in ret3:
        if int(row[1]) < 10:
            break
        num_rows = num_rows + 1
        hoverBackgroundColor3.append(randomColor())
        data3.append({
            'label': row[0],
            'value': int(row[1]),
        })





    #人员伤亡
    hoverBackgroundColor4 = []
    data4 = []
    num_rows = 0
    sql = f"SELECT task_id,count(*) as count from category where category='people' and (task_id={'or task_id='.join(earthquake_id)});"
    cursor.execute(sql)
    ret3 = cursor.fetchall()
    for row in ret3:
        num_rows = num_rows + 1
        hoverBackgroundColor4.append(randomColor())
        data4.append({
            'label': "地震",
            'value': int(row[1]),
        })
    sql = f"SELECT task_id,count(*) as count from category where category='people' and (task_id={'or task_id='.join(typhoon_id)});"
    cursor.execute(sql)
    ret3 = cursor.fetchall()
    for row in ret3:
        num_rows = num_rows + 1
        hoverBackgroundColor4.append(randomColor())
        data4.append({
            'label': "台风",
            'value': int(row[1]),
        })
    sql = f"SELECT task_id,count(*) as count from category where category='people' and (task_id={'or task_id='.join(rainstorm_id)});"
    cursor.execute(sql)
    ret3 = cursor.fetchall()
    for row in ret3:
        num_rows = num_rows + 1
        hoverBackgroundColor4.append(randomColor())
        data4.append({
            'label': "暴雨",
            'value': int(row[1]),
        })
        # 房屋损失
        hoverBackgroundColor5 = []
        data5 = []
        num_rows = 0
        sql = f"SELECT task_id,count(*) as count from category where category='house' and (task_id={'or task_id='.join(earthquake_id)});"
        cursor.execute(sql)
        ret3 = cursor.fetchall()
        for row in ret3:
            num_rows = num_rows + 1
            hoverBackgroundColor5.append(randomColor())
            data5.append({
                'label': "地震",
                'value': int(row[1]),
            })
        sql = f"SELECT task_id,count(*) as count from category where category='house' and (task_id={'or task_id='.join(typhoon_id)});"
        cursor.execute(sql)
        ret3 = cursor.fetchall()
        for row in ret3:
            num_rows = num_rows + 1
            hoverBackgroundColor5.append(randomColor())
            data5.append({
                'label': "台风",
                'value': int(row[1]),
            })
        sql = f"SELECT task_id,count(*) as count from category where category='house' and (task_id={'or task_id='.join(rainstorm_id)});"
        cursor.execute(sql)
        ret3 = cursor.fetchall()
        for row in ret3:
            num_rows = num_rows + 1
            hoverBackgroundColor5.append(randomColor())
            data5.append({
                'label': "暴雨",
                'value': int(row[1]),
            })

        # 财产损失
        hoverBackgroundColor6 = []
        data6 = []
        num_rows = 0
        sql = f"SELECT task_id,count(*) as count from category where category='properties' and (task_id={'or task_id='.join(earthquake_id)});"
        cursor.execute(sql)
        ret3 = cursor.fetchall()
        for row in ret3:
            num_rows = num_rows + 1
            hoverBackgroundColor6.append(randomColor())
            data6.append({
                'label': "地震",
                'value': int(row[1]),
            })
        sql = f"SELECT task_id,count(*) as count from category where category='properties' and (task_id={'or task_id='.join(typhoon_id)});"
        cursor.execute(sql)
        ret3 = cursor.fetchall()
        for row in ret3:
            num_rows = num_rows + 1
            hoverBackgroundColor6.append(randomColor())
            data6.append({
                'label': "台风",
                'value': int(row[1]),
            })
        sql = f"SELECT task_id,count(*) as count from category where category='properties' and (task_id={'or task_id='.join(rainstorm_id)});"
        cursor.execute(sql)
        ret3 = cursor.fetchall()
        for row in ret3:
            num_rows = num_rows + 1
            hoverBackgroundColor6.append(randomColor())
            data6.append({
                'label': "暴雨",
                'value': int(row[1]),
            })

        # 交通损失
        hoverBackgroundColor7 = []
        data7 = []
        num_rows = 0
        sql = f"SELECT task_id,count(*) as count from category where category='transport' and (task_id={'or task_id='.join(earthquake_id)});"
        cursor.execute(sql)
        ret3 = cursor.fetchall()
        for row in ret3:
            num_rows = num_rows + 1
            hoverBackgroundColor7.append(randomColor())
            data7.append({
                'label': "地震",
                'value': int(row[1]),
            })
        sql = f"SELECT task_id,count(*) as count from category where category='transport' and (task_id={'or task_id='.join(typhoon_id)});"
        cursor.execute(sql)
        ret3 = cursor.fetchall()
        for row in ret3:
            num_rows = num_rows + 1
            hoverBackgroundColor7.append(randomColor())
            data7.append({
                'label': "台风",
                'value': int(row[1]),
            })
        sql = f"SELECT task_id,count(*) as count from category where category='transport' and (task_id={'or task_id='.join(rainstorm_id)});"
        cursor.execute(sql)
        ret3 = cursor.fetchall()
        for row in ret3:
            num_rows = num_rows + 1
            hoverBackgroundColor7.append(randomColor())
            data7.append({
                'label': "暴雨",
                'value': int(row[1]),
            })

        # 农业损失
        hoverBackgroundColor8 = []
        data8 = []
        num_rows = 0
        sql = f"SELECT task_id,count(*) as count from category where category='agriculture' and (task_id={'or task_id='.join(earthquake_id)});"
        cursor.execute(sql)
        ret3 = cursor.fetchall()
        for row in ret3:
            num_rows = num_rows + 1
            hoverBackgroundColor8.append(randomColor())
            data8.append({
                'label': "地震",
                'value': int(row[1]),
            })
        sql = f"SELECT task_id,count(*) as count from category where category='transport' and (task_id={'or task_id='.join(typhoon_id)});"
        cursor.execute(sql)
        ret3 = cursor.fetchall()
        for row in ret3:
            num_rows = num_rows + 1
            hoverBackgroundColor8.append(randomColor())
            data8.append({
                'label': "台风",
                'value': int(row[1]),
            })
        sql = f"SELECT task_id,count(*) as count from category where category='transport' and (task_id={'or task_id='.join(rainstorm_id)});"
        cursor.execute(sql)
        ret3 = cursor.fetchall()
        for row in ret3:
            num_rows = num_rows + 1
            hoverBackgroundColor8.append(randomColor())
            data8.append({
                'label': "暴雨",
                'value': int(row[1]),
            })

    context = {
        'earthquake_brief': earthquake_brief,
        'earthquake_information': earthquake_information,
        'typhoon_brief': typhoon_brief,
        'typhoon_information': typhoon_information,
        'rainstorm_brief': rainstorm_brief,
        'rainstorm_information': rainstorm_information,
        'datajson': json.dumps(data),
        'hoverjson': json.dumps(hoverBackgroundColor),
        'datajson2': json.dumps(data2),
        'hoverjson2': json.dumps(hoverBackgroundColor2),
        'datajson3': json.dumps(data3),
        'hoverjson3': json.dumps(hoverBackgroundColor3),
        'datajson4': json.dumps(data4),
        'hoverjson4': json.dumps(hoverBackgroundColor4),
        'datajson5': json.dumps(data5),
        'hoverjson5': json.dumps(hoverBackgroundColor5),
        'datajson6': json.dumps(data6),
        'hoverjson6': json.dumps(hoverBackgroundColor6),
        'datajson7': json.dumps(data7),
        'hoverjson7': json.dumps(hoverBackgroundColor7),
        'datajson8': json.dumps(data8),
        'hoverjson8': json.dumps(hoverBackgroundColor8),
    }
    return  render(request,'statistical.html',context)
def map_(request):
    context = {

    }
    return render(request, 'map_.html', context)
def map_2(request):
    context = {

    }
    return render(request, 'map_2.html', context)
def map_3(request):
    context = {

    }
    return render(request, 'map_3.html', context)
#地震
@csrf_exempt
def map_1_collect(request):
    task_id = [i.replace("'", "") for i in earthquake_id]
    task_id = '-'.join(task_id)
    province = str(request.POST["province"])
    cursor = connection.cursor()
    sql = f"select distinct cluster from `event` where (task_id={'or task_id='.join(earthquake_id)}) and province like '%{province}%' order by cluster;"
    cursor.execute(sql);
    res = cursor.fetchall()
    context = []
    for cluster in res:
        print(cluster)
        provinces = []
        citys = []
        areas = []
        events = []
        event_time = ""
        cluster = str(cluster[0])
        # sql = f"select post_id,province,city,area,`time`,`event` from `event` where (task_id={'or task_id='.join(earthquake_id)}) and province like '%{province}%' and cluster = '{cluster}';"
        sql = f"select post_id,province,city,area,doc_t,info from authority where (task_id={'or task_id='.join(earthquake_id)}) and province like '%{province}%' and number = '{cluster}';"

        cursor.execute(sql);
        ret = cursor.fetchall()
        print(ret)
        for i in (ret):
            if event_time == "":
                event_time = str(i[4])
            provinces.append(i[1])
            citys.append(i[2])
            areas.append(i[3])
            events.append(i[5])
        province_ = ""
        for k,v in collections.Counter(provinces).most_common(3):
            if (k != None and k != '') and province_ == '':
                province_ = k
                break
        city_ = ""
        for k, v in collections.Counter(citys).most_common(3):
            if (k != None and k != '') and city_ == '':
                city_ = k
                break
        area_ = ""
        for k, v in collections.Counter(areas).most_common(3):
            if (k != None and k != '') and area_ == '':
                area_ = k
                break
        event_ = ""
        for k, v in collections.Counter(events).most_common(3):
            if (k != None and k != '') and event_ == '':
                event_ = k
                break
        if event_ != '':
            tmp = {
                "task_id": task_id,
                'clus': cluster,
                "province": province_,
                "city": city_,
                "area": area_,
                "time": event_time,
                "event": event_
            }
            context.append(tmp)
    context = json.dumps(context, ensure_ascii=False)
    return HttpResponse(context)
#台风
@csrf_exempt
def map_2_collect(request):
    task_id = [i.replace("'", "") for i in typhoon_id]
    task_id = '-'.join(task_id)
    province = str(request.POST["province"])
    cursor = connection.cursor()
    sql = f"select distinct cluster from `event` where (task_id={'or task_id='.join(typhoon_id)}) and province like '%{province}%' order by cluster;"
    cursor.execute(sql);
    res = cursor.fetchall()
    context = []
    for cluster in res:
        provinces = []
        citys = []
        areas = []
        events = []
        event_time = ""
        cluster = str(cluster[0])
        sql = f"select post_id,province,city,area,`time`,`event` from `event` where (task_id={'or task_id='.join(typhoon_id)}) and province like '%{province}%' and cluster = '{cluster}';"
        cursor.execute(sql);
        ret = cursor.fetchall()
        for i in (ret):
            if event_time == "":
                event_time = str(i[4])
            provinces.append(i[1])
            citys.append(i[2])
            areas.append(i[3])
            events.append(i[5])
        province_ = ""
        for k, v in collections.Counter(provinces).most_common(3):
            if (k != None and k != '') and province_ == '':
                province_ = k
                break
        city_ = ""
        for k, v in collections.Counter(citys).most_common(3):
            if (k != None and k != '') and city_ == '':
                city_ = k
                break
        area_ = ""
        for k, v in collections.Counter(areas).most_common(3):
            if (k != None and k != '') and area_ == '':
                area_ = k
                break
        event_ = ""
        for k, v in collections.Counter(events).most_common(3):
            if (k != None and k != '') and event_ == '':
                event_ = k
                break
        if event_ != '':
            tmp = {
                "task_id": task_id,
                'clus': cluster,
                "province": province_,
                "city": city_,
                "area": area_,
                "time": event_time,
                "event": event_
            }
            context.append(tmp)
    context = json.dumps(context, ensure_ascii=False)
    return HttpResponse(context)
#暴雨
@csrf_exempt
def map_3_collect(request):
    task_id = [i.replace("'","") for i in rainstorm_id]
    task_id = '-'.join(task_id)
    province = str(request.POST["province"])
    cursor = connection.cursor()
    sql = f"select distinct cluster from `event` where (task_id={'or task_id='.join(rainstorm_id)}) and province like '%{province}%' order by cluster;"
    cursor.execute(sql);
    res = cursor.fetchall()
    context = []
    for cluster in res:
        provinces = []
        citys = []
        areas = []
        events = []
        event_time = ""
        cluster = str(cluster[0])
        sql = f"select post_id,province,city,area,`time`,`event` from `event` where (task_id={'or task_id='.join(rainstorm_id)}) and province like '%{province}%' and cluster = '{cluster}';"
        cursor.execute(sql);
        ret = cursor.fetchall()
        for i in (ret):
            if event_time == "":
                event_time = str(i[4])
            provinces.append(i[1])
            citys.append(i[2])
            areas.append(i[3])
            events.append(i[5])
        province_ = ""
        for k, v in collections.Counter(provinces).most_common(3):
            if (k != None and k != '') and province_ == '':
                province_ = k
                break
        city_ = ""
        for k, v in collections.Counter(citys).most_common(3):
            if (k != None and k != '') and city_ == '':
                city_ = k
                break
        area_ = ""
        for k, v in collections.Counter(areas).most_common(3):
            if (k != None and k != '') and area_ == '':
                area_ = k
                break
        event_ = ""
        for k, v in collections.Counter(events).most_common(3):
            if (k != None and k != '') and event_ == '':
                event_ = k
                break
        if event_ != '':
            tmp = {
                "task_id": task_id,
                'clus': cluster,
                "province": province_,
                "city": city_,
                "area": area_,
                "time": event_time,
                "event": event_
            }
            context.append(tmp)
    context = json.dumps(context, ensure_ascii=False)
    return HttpResponse(context)