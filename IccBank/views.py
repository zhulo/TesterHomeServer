from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from django.core.paginator import Paginator


def blog_list(request):
    content = {}
    content['blogs'] = "aaa"
    return render_to_response('blog_detail.html', content)


# def postTest2(request):
#     uname = request.POST['uname']
#     upwd = request.POST['upwd']
#     ugender = request.POST['ugender']
#     uhobby = request.POST.getlist('uhobby')
#     context = {'uname': uname, 'upwd': upwd, 'ugender': ugender, 'uhobby': uhobby}
#     return render(request, 'booktest/postTest2.html', context)


from django.http import HttpResponse
import json


# 定义功能
def add_args(a, b):
    return a + b


# 接口函数
def post_request(request):
    if request.method == 'POST':  # 当提交表单时
        dic = {}
        # 判断是否传参
        if request.POST:
            a = request.POST.get('a', 0)
            b = request.POST.get('b', 0)
            print(a)
            print(b)
            # 判断参数中是否含有a和b
            if a and b:
                res = add_args(int(a), int(b))
                dic['number'] = res
                dic = json.dumps(dic)
                return HttpResponse(dic)
            else:
                return HttpResponse('输入错误')
        else:
            return HttpResponse('输入为空')

    else:
        return HttpResponse('方法错误')