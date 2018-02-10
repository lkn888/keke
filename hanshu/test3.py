# coding:utf-8
import requests,time
import unittest
import re
#参数化的操作
url="http://127.0.0.1/zentao/user-login.html"
def login(s,usr,pwd):

            h={
                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
                "Accept-Language":"zh-CN,zh;q=0.8",
                "Accept-Encoding":"gzip, deflate, sdch",
                "Connection":"keep-alive",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            }
            body1={
                 "account": usr,
                 "password":pwd,
                 "referer" : "",
            }


            r1=s.post(url,data=body1,headers=h)
            return  r1.content
def login_result(res):
          if "登录失败，请检查您的用户名或密码是否填写正确。" in res:
                 return False
          elif "parent.location" in res:
                 return True
          else:
           return False


if __name__=="__main__":
    usr="admin"
    pwd="123456"
    s=requests.session()  #不要写死
    a=login(s,usr,pwd)
    print a
    print login_result(a)




