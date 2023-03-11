# 密碼重試程式
# 設定好密碼 password = 'a123456'
# 最多輸入3次
# 不對的話印出密碼錯誤，還有_次機會
# 對的話印出'登入成功'

n = 0
password = 'a123456'

while n < 3:
    pwd = input('請輸入密碼 : ')
    n += 1
    if pwd == password:
        print('登入成功')
        break
    else:
        if 3-n > 0:
            print('密碼錯誤，你還有', 3-n, '次機會')
        else:
            print('你被鎖了，傻B')
