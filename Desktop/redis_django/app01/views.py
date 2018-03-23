from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from django_redis import get_redis_connection


def index(request):
    '''进入首页'''
    # 连接redis数据库，返回一个strictredis的对象
    # default：表示setting文件中的caches
    sr = get_redis_connection('default')

    # 保存一个string类型的键值对
    sr.set('username','python')
    sr.set('verify_code','123456')

    # 获取string类型的值
    username = sr.get('username').decode()
    verify_code = sr.get('verify_code').decode()

    text = '姓名：%s  验证码：%s' %(username,verify_code)
    return HttpResponse(text)


def set_session(request):
    '''保存session数据'''
    request.session['username'] = 'Django'
    request.session['verify_code'] = '123456'
    return HttpResponse('保存数据成功')


def get_session(request):
    '''获取session数据'''
    username = request.session.get('username')
    verify_code = request.session.get('verify_code')
    text = 'username:%s verify_code:%s' %(username,verify_code)
    return HttpResponse(text)