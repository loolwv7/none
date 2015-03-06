                  Linux中如何识别硬件并编译相关内核模块

如果想想为自己的电脑编译一个适合自己的精减内核，比如只增加自己需要的功能模块、指定使用何种驱动、额外的补丁等等，在Linux系统中这是可以办到的。
具体方法也比较简单---前提是对Linux系统有了基本的了解。方法如下：

1) 首先列出机器上的PCI设备

查看详细信息：lspci -tvnn 或 lspci -vv

也可以看一下加载了哪些模块:

lsmod

2) 把"lspci -n"命令的输出COPY到这个网站中http://kmuto.jp/debian/hcl/index.cgi 的空白框里，"Check"一下自己的电脑需要用到哪些驱动，然后根据输出寻找模块所在位置。

比如列表中的82567LM Gigabit Network Connection网卡需要e1000e的驱动模块，那么在编译内核时网卡驱动的那一栏目中只需要勾选它。
如果不知道这个驱动的具体位置可以搜索一下内核配制文件

$ grep -i -n e1000e /path_to/linux/.config
1267:CONFIG_E1000E=m

可以看出它在内核配制文件中的1267行，然后你可以在相关位置找到它并选择合适的编译方式，以此类推。
也可以手动修改config文件，比如你想直接编译到内核启动文件中而不以模块形式加载，那么把上面的改为:

CONFIG_E1000E=y

3) 如果当前内核源码不包含该设备驱动但有相关补丁发布（确认有该补丁），下载回来后放到内核源码目录。

cd /usr/src/linux
patch -p1 < patch_name
make && make modules_install make install

在没有定制之前，各发行版默认几乎会把所有可能的模块编译进去以适应不同的机器设备（模块文件夹高达数十兆）。
而在自己定制之后，就只需要很小的内核文件或模块文件（通常只有几兆大小）便可以了，而且自己定制编译内核时还可以在选择启动中加载额外的ROM文件，适应不同的需要。

如何通过机器的PCI ID查询该PCI设备使用得是什么模块呢？
举个例子，比如查看本机无线网卡。

# lspci -nn | grep -i wireless
0c:00.0 Network controller [0280]: Atheros Communications Inc. AR9287 Wireless
Network Adapter (PCI-Express) [168c:002e] (rev 01)

以上结果中参数的含义：
0c:00.0 硬件ID
168c 设备制造商
002e 设备型号ID

# grep "002e" /lib/modules/3.3.3-smp/modules.pcimap
ath9k 0x0000168c 0x0000002e 0xffffffff 0xffffffff 0x00000000 0x00000000 0x0

就可以通过设备型号ID在modules.pcimap文件中找到该无线网卡使用了ath9k驱动模块。
