H3C 3600 
1, b

console 密码忘记了。

H3C设备认证模式默认是scheme,也就是在local-user里的用户和密码。

需要在user-interface vty 0 4接口下，输入“set authentication mode password”，然后新加的密码才生效>

<H3C>system-view

[H3C]user-interface aux 0

[H3C-ui-aux0]authentication-mode password

[H3C-ui-aux0]set authenticaton password simple 123456

只用密码的用户认证

[H3C]user-interface vty 0 4

[H3C-ui-vty0-4]authentication-mode password

[H3C-ui-vty0-4]set authentication password simple 123456




例1：用console口进行TELNET密码、命令级别设置

[H3C] user-interface vty 0 4                                                     //进入vty用户视图

[H3C-ui-vty0-4] authentication-mode password                       //在vty用户视图设置

[H3C-ui-vty0-4] set authentication password simple 123456   //设置明文密码

[H3C -ui-vty0-4]user  privilege level 3                                     //设置命令级别 

 

 例2：用console口进行TELNET用户名、密码、命令级别设置

 [H3C]user-interface vty 0 4                                                       //进入vty用户视图

 [H3C -ui-vty0-4]authentication-mode scheme                          //进行用户名称＋口令方式进行配置

 [H3C]local-user test                                                                 // 设置本地用户名为test

 [H3C -user-test]service-type telnet level 3                              //设置test用户命令级别为3

 [H3C -user-test]password simple 123456                               //设置test用户密码为123456

例3：TELNET登录后对用户test修改口令

[H3C] local-user test                                                               //进入test用户视图

[H3C -user-test]service-type telnet level 3                            //如果少此步，则不能进行口令修改

[H3C -user-test]password simple test999                             //修改test用户密码为test999


1, dis cur | begin ip route
2, ping gateway
3, tracert 8.8.8.8
4, find next
5, 


Result:
port: 16,17,18,19,20
gw:192.168.37.1
