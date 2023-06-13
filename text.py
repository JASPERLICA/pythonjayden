import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

host, port = ("127.0.0.1",89898)
print(type(host))
print(type(port))
print(host)
print(host,port)
r,g,b = ["red","green","blue"]
print(type(r))
print(r,g,b)
print("abc",end = "")
print("edf",end = "")
a = "2.33"
print("")
print(a)
print("the type of a is:",type(a))
bb = float(a)
cc = bb + 3
print(cc)
print("the type of bb is:",type(bb))

