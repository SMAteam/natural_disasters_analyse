# import json
# import jieba
# from .predict import Predictor
# with open(,"r") as fr:
#     config = json.load(fr)
#
# for content in text:
#     if "周震南" in content or '蜕变之战' in content or '台团综' in content or '转发微博' in content or '舞台' in content:
#         print("false")
#         try:
#             c.execute("insert into typhoon_false(weibo_id,user_id,time,"
#                                                                    "category,original_text) values (?,?,?,?,?)",(format(content[0]),format(content[1]),format(content[2]),format(content[3]),format(content[4])))
#             conn.commit()
#         except:
#             continue
#     elif '台风' not in content:
#         print("false")
#         try:
#             c.execute("insert into typhoon_originaltext(weibo_id,user_id,time,"
#                                                                    "category,original_text) values (?,?,?,?,?)",(format(content[0]),format(content[1]),format(content[2]),format(content[3]),format(content[4])))
#             conn.commit()
#         except:
#             continue
#     else:
#         inputs.append(content)
#
# # text = " ".join([" ".join(jieba.lcut(line)) for line in data])
#
# predictor = Predictor(config)
#
# #total = len(labels)
# #print(set(labels))
# corr = 0
# for i in range(len(inputs)):
#     result = predictor.predict([item for item in jieba.cut(inputs[i][4], cut_all=False)])
#     if(result=='1'):
#         print(inputs[i],"正确")
#         try:
#             c.execute("insert into typhoon_originaltext(weibo_id,user_id,time,"
#                                                                    "category,original_text) values (?,?,?,?,?)",(format(inputs[i][0]),format(inputs[i][1]),format(inputs[i][2]),format(inputs[i][3]),format(inputs[i][4])))
#             conn.commit()
#         except:
#             continue
#     else:
#         print(inputs[i],"错误")
#         try:
#             c.execute("insert into typhoon_false(weibo_id,user_id,time,"
#                                                                    "category,original_text) values (?,?,?,?,?)",(format(inputs[i][0]),format(inputs[i][1]),format(inputs[i][2]),format(inputs[i][3]),format(inputs[i][4])))
#             conn.commit()
#         except:
#             continue
#     #print(inputs[i])
#     #print(result)
# #    if result == labels[i]:
# #        corr += 1
# #    else:
# #        print(inputs[i])
# #print(corr / total)
#
