from django.http import HttpResponse

from Icncde.common.service import email_access_token


def post_email_access_token(request):
    content = {}
    if request.POST:
        login_email = request.POST.get('login_email', 0)
        password = request.POST.get('password', 0)
        if login_email and password:
            content = email_access_token(login_email, password)
            return HttpResponse(str(content))
        else:
            return HttpResponse("入参错误")
    else:
        return HttpResponse("请求方法错误")
