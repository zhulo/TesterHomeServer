import conf
class EnvironmentTest:
    IcncdeHost = "http://test.mobile.icctoro.com:7007"
    UsersList = ['open0001@qq.com', 'open0002@qq.com', 'open0003@qq.com', 'open0004@qq.com', 'open0005@qq.com']
    PasswordToMd5 = "6846860684f05029abccc09a53cd66f1"  # a111111


class EnvironmentOnline:
    IcncdeHost = "http://icctoro.com:7007"
    UsersList = []
    PasswordToMd5 = "6846860684f05029abccc09a53cd66f1"  # a111111


class RequestApiBaseParam:
    Headers = {"Accept": "application/json", "Content-Language": "zh-cn", "Source-Site": "pc.jys", "userId": "",
               "Content-Type": "application/x-www-form-urlencoded", "Authorization": ""}


class GlobalConfig:
    if conf.DebugEnvironment.upper() == 'TEST':
        Environment = EnvironmentTest()
    elif conf.DebugEnvironment.upper() == 'ONLINE':
        Environment = EnvironmentOnline()


if __name__ == '__main__':
    print(GlobalConfig.Environment.IcncdeHost)