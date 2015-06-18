前期准备：
关闭所有连接该光交的应用服务。

1、通过串口线连接至EMC MDS9124管理口，打开HyperTerminal/Minicom程序，设置连接如下：
Bits per second: 9600
Data bits: 8
Parity: None
Stop bits: 1
Flow control: None
(注：如果是MDS9500系列则把Bits设置为38400)

2、由于密码已忘记，手动按电源重启EMC光纤交换机。
3、交换机重启进入SANOS时，按住Ctrl+]键使交换机进入到boot模式

switch(boot)#

4、切换到配制模式，并更改密码。
switch(boot)# configure terminal
switch(bootconfig)# adminpassword PASSWORD
switch(bootconfig)# exit

5、加载启动映像进入正常模式。
switch(boot)# load bootflash:SANIOS.img

6、保存配制信息即完成，登录使用新密码测试。
switch# copy runningconfig startupconfig

最后：应用服务器主机重新扫描磁盘，识别正常后，开启相应服务即可。
cfgmgr -v
lsdev -Ccdisk

