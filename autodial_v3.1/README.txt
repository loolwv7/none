1) 首先确认安装了Chrome浏览器
（经测试在WINDOWS下与IE，Firefox相比，这个性能更好。）

-> 开始-设置-网络连接中创建一个新的连接（pppoe方式），
ISP名称填写PPPOE，不用填写帐户名和密码！

修改run.bat脚本中的宽带拨号用户名和密码。

RASDIAL PPPOE username password


2) 把autodial脚本程序目录放入C:\
   把wget_for_windows目录中的文件全部放入C:\WINDOWS\SYSTEM32目录中。


3) 运行run.bat,　在弹出的窗口中填写日期和自动拨号的时间间隔即可。
（填写某一天的时间格式为"201304/03"，多天的格式为"201304/03|201304/04" ，日期中间加个"|"符号隔开。）
