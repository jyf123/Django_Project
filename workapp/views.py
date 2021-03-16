import os
from django.shortcuts import render, HttpResponse
import  json
# Create your views here.

# 添加 index 函数，返回 index.html 页面
def index(request):
    return render(request, 'index.html')

def sub0(request):
    return render(request, 'index.html')

def sub1(request):
    return render(request, 'charts.html')

def sub2(request):
    return render(request, 'panels.html')

def sub3(request):
    return render(request, 'notifications.html')

def sub4(request):
    return render(request, 'page-lockscreen.html')

def sub5(request):
    return render(request, 'page-login.html')

def sub6(request):
    view_name = "Joe Bidden"
    view_relationship = [["妻子","吉尔·拜登"],
                    ["儿子","亨特·拜登"],
                    ["儿子","傅·拜登"],
                    ["弟弟","詹姆斯·拜登"]]#关系不固定有几个，而且可能有好几个儿子，所以用字典的时候可能会有重名的问题
    view_label = {"sports":0,
             "foods":0,
             "politic":1,
             "military":1}#这些标签是固定的，用0/1代表有/没有，


    # chart_options = {
    #     'title': 'ECharts 入门示例',
    #     'legend':  ['销量'],
    #     'xAxis:': ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
    #     'series': ['销量', 'bar',[5, 20, 36, 10, 10, 20]] #name type data
    # }#传不过去
    #
    # result = {"name":json.dumps(view_name),
    #           "relationship":json.dumps(view_relationship) ,#前端直接relationship.key的名字即可提取
    #           "label":json.dumps(view_label),
    #           "option":json.dumps(chart_options),
    #           }#传递复杂数据对象不行, 无法解析



    #echarts表格数据，无法整合到一个大的集合里，无法解析，目前只能一个一个传入
    title = 'ECharts 入门示例'
    legend = ['销量']
    xAxis = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    series = ['销量', 'bar',[5, 20, 36, 10, 10, 20]] #传递复杂数据对象不行

    title2 = {
               'text': '某站点用户访问来源',
               'subtext': '纯属虚构',
               'left': 'center'
           },

    itemstyle = {'itemStyle': {
                            'shadowBlur': 10,
                            'shadowOffsetX': 0,
                            'shadowColor': 'rgba(0, 0, 0, 0.5)'
                        }}# 无法解析

    data = [
              {'value': 1048, 'name': '搜索引擎'},
            {'value': 735, 'name': '直接访问'},
            {'value': 580, 'name': '邮件营销'},
            {'value': 484, 'name': '联盟广告'},
            {'value': 300, 'name': '视频广告'}
              ]#
    data_value = [ 1048, 735, 580, 484, 300]
    data_name = ['搜索引擎','直接访问','邮件营销','联盟广告','视频广告']

    result = {"name":json.dumps(view_name),
              "relationship":json.dumps(view_relationship) ,#前端直接relationship.key的名字即可提取
              "label":json.dumps(view_label),
              "title":json.dumps(title),
              "legend":json.dumps(legend),
              "xAxis":json.dumps(xAxis),
              "series":json.dumps(series),
              "title2":json.dumps(title2),
              "datavalue":json.dumps(data_value),
              "dataname":json.dumps(data_name)
              }

    return render(request, 'page-profile.html', result)

def sub7(request):
    return render(request, 'typography.html')

def sub8(request):
    return render(request, 'elements.html')

def sub9(request):
    return render(request, 'tables.html')

def sub10(request):
    return render(request, 'icons.html')

def sub11(request):
    return render(request, 'page-charts.html')

def sub12(request):
    data = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    return render(request, 'test.html',{'datas':json.dumps(data)})

def sub13(request):
    basic_info = [{"name":"特朗普"},
                  {"birthday":"1946年6月14日"},
                  {"country":"美国"},
                  {"nation":"德意志人"}]
    eduction_ex = ["纽约军事学院","福坦莫大学","宾夕法尼亚大学沃顿商学院"]
    work_ex = ["从商","演艺","从政"]
    bidata = [basic_info,eduction_ex,work_ex]
    return render(request,'people.html',{"test":bidata})

def sub14(request):
    return render(request,'search.html')

# def upload1(request):
#     return render(request, 'sub1.html')