from django.http import HttpResponse

from IccBank.wallet.service import WalletApi


def post_create_address(request):
    content = {}
    if request.POST:
        currency_code = request.POST.get('currency_code', 0)
        count = request.POST.get('count', 0)
        if currency_code and count:
            content = WalletApi().create_address(currency_code, count)
            return HttpResponse(str(content))
        else:
            return HttpResponse("入参错误")
    else:
        return HttpResponse("请求方法错误")


def post_check_address(request):
    content = {}
    if request.POST:
        currency_code = request.POST.get('currency_code', 0)
        address = request.POST.get('address', 0)
        if currency_code and address:
            content = WalletApi().check_address(currency_code, address)
            return HttpResponse(str(content))
        else:
            return HttpResponse("入参错误")
    else:
        return HttpResponse("请求方法错误")


def post_add_address(request):
    content = {}
    if request.POST:
        currency_code = request.POST.get('currency_code', 0)
        address = request.POST.get('address', 0)
        if currency_code and address:
            content = WalletApi().add_address(currency_code, address)
            return HttpResponse(str(content))
        else:
            return HttpResponse("入参错误")
    else:
        return HttpResponse("请求方法错误")


def post_agentPay_proxyPay(request):
    if request.POST:
        currency_code = request.POST.get('currency_code', 0)
        address = request.POST.get('address', 0)
        amount = request.POST.get('amount', 0)
        if currency_code and address and amount:
            content = WalletApi().agentPay_proxyPay(currency_code, address, amount)
            return HttpResponse(str(content))
        else:
            return HttpResponse("入参错误")
    else:
        return HttpResponse("请求方法错误")


def post_agentPay_query(request):
    if request.POST:
        userBizId = request.POST.get('userBizId', 0)
        if userBizId:
            content = WalletApi().agentPay_query(userBizId)
            return HttpResponse(str(content))
        else:
            return HttpResponse("入参错误")
    else:
        return HttpResponse("请求方法错误")
