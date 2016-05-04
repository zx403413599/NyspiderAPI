from spider.renrendai import *

def test():
    work=Renrendai('18502793163','DqdyNBGDpQGFEhkQ4CFqz3x3xXsJyZeo3w+M5ikpD07V1YGNC6CIJxRUDmWlQA0ze1tli0h+0CV/0DwZ4yzpH9a8CL5SCYz2z+Cf7I0adTdGCMQxIMglXm/ouG+loJklRzFe+H6tbR48qE9d4FksNXJBKC91JDGjdWMaaInrHos=')
    infor=work.getLoan(1000)
    print(infor)
test()
