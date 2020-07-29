import os
from django.db.models import Count
from django.db.models.functions import ExtractYear, ExtractMonth
earthquake_id = ['\'1_1\'']
typhoon_id = ['\'1_2\'']
rainstorm_id = ['\'1_3\'']
from django.shortcuts import render
from .models import weibo_post,noise_judge,category,event
import json
import random
from django.db import connection
from django.core.paginator import Paginator
cursor = connection.cursor()
def home(request):
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
    print(data)
    for row in ret3:
        if str(row[0]) not in data:
            data[str(row[0])] = [0,0,int(row[1])]
        else:
            print(data[str(row[0])])
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
    return render(request, 'home.html',context)
def history(request):
    type = request.GET['type']
    relevant = request.GET['relevant']
    if type == '0' and relevant == '0':
        sql = f"select weibo_post.post_id,noise,post_time,post_content from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id order by post_time DESC limit 1000;"
    elif type == '1' and relevant == '0':
        sql = f"select weibo_post.post_id,noise,post_time,post_content from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and (noise_judge.task_id={'or noise_judge.task_id='.join(earthquake_id)}) order by post_time DESC limit 1000;"
    elif type == '2' and relevant == '0':
        sql = f"select weibo_post.post_id,noise,post_time,post_content from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and (noise_judge.task_id={'or noise_judge.task_id='.join(typhoon_id)}) order by post_time DESC limit 1000;"
    elif type == '3' and relevant == '0':
        sql = f"select weibo_post.post_id,noise,post_time,post_content from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and (noise_judge.task_id={'or noise_judge.task_id='.join(rainstorm_id)}) order by post_time DESC limit 1000;"

    elif type == '0' and relevant == '1':
        sql = f"select weibo_post.post_id,noise,post_time,post_content from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and noise='1' order by post_time DESC limit 1000;"
    elif type == '1' and relevant == '1':
        sql = f"select weibo_post.post_id,noise,post_time,post_content from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and (noise_judge.task_id={'or noise_judge.task_id='.join(earthquake_id)}) and noise='1' order by post_time DESC limit 1000;"
    elif type == '2' and relevant == '1':
        sql = f"select weibo_post.post_id,noise,post_time,post_content from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and (noise_judge.task_id={'or noise_judge.task_id='.join(typhoon_id)}) and noise='1' order by post_time DESC limit 1000;"
    elif type == '3' and relevant == '1':
        sql = f"select weibo_post.post_id,noise,post_time,post_content from weibo_post,noise_judge where weibo_post.post_id=noise_judge.post_id and weibo_post.task_id=noise_judge.task_id and (noise_judge.task_id={'or noise_judge.task_id='.join(rainstorm_id)}) and noise='1' order by post_time DESC limit 1000;"
    cursor.execute(sql)
    ret = cursor.fetchall()
    isnoise = []
    weibo_id = []
    time = []
    text = []
    num_rows = 0
    page_one =[]
    for row in ret:
        num_rows+=1
        isnoise.append(row[1])
        weibo_id.append(row[0])
        time.append(str(row[2])[:10])
        text.append(row[3])
        if num_rows<=15:
            record = {
                'isnoise': row[1],
                'num_rows':num_rows-1,
                'weibo_id': row[0],
                'original_text':row[3][3:],
                'time': str(row[2])[:10]
            }
            page_one.append(record)
    context = {
        'weibojson': json.dumps(weibo_id),
        'timejson': json.dumps(time),
        'textjson': json.dumps(text),
        'isnoisejson': json.dumps(isnoise),
        'page_one': page_one,
    }
    return render(request, 'history.html',context)
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
def statistical(request):
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
        print(int(row[1]))
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
        print(int(row[1]))
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
        print(int(row[1]))

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