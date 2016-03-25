 在拨号界面输入*#*#4636#*#*搜索 选择手机信息，划到最下面，那就可以看到了 


当我们刷机的时候实际上是要刷以下几个部分
bootloader：其实这个东西就是我们手机最底层的一个东西，可以理解为一个简单的系统，当我们开机按下音量键的时候就入的就是他
radio         ：这个东西实际上是负责电话的信号射频之类的管理。
boot         ： 这个东西实际上是进入系统之前的一个引导，会对硬件驱动之类的进行加电检查，没有问题后他会把系统镜像加载进来，然后把权限交给系统，这样就进入系统。
system      ：很明显，这个就是系统，你可以理解为window的XP，或者win7之类
cache        ：存放缓存信息
userdata   ：存放用户数据，比如你安装的程序和对应的数据。
recovery   ：如果你装过windos操作系统，他就是dos工具箱或者是一键还原之类的东西。

    刷机包分析

当我们拿到一个工厂镜像文件他的扩展名是tgz，例如shamu-lmy47z-factory-33951732.tgz, 其实他是一个压缩包，我们可以解压出来。解压后变成shamu-lyz28e-factory-b542b88a.tar， 然后再解压包含下面东西

    bootloader-shamu-moto-apq8084-71.10.img   //这就是bootloader的镜像文件
    flash-all.bat                                                       //这个windows下脚本文件，把整个镜像文件刷进去
    flash-all.sh                                                        //这个应该是linux下脚本文件，把整个镜像文件刷进去
    flash-base.sh                                                     //这个应该是linux下脚本文件，只刷bootloader和raido
    image-shamu-lyz28e.zip                                   //这个是系统压缩包，不是镜像文件
    radio-shamu-d4.01-9625-05.14+fsg-9625-02.93.img //radio 的镜像文件。


从上面我们可以看到，其实当我们解压后，里面已经给我们提供了刷机脚本，理论上说我们机器安装了驱动和adb工具后直接可以把他们放在adb下，然后双击flash-all.bat就会自动刷机了。老虫的工具应该也是解压后然后再做处理。
其实，我们可以更灵活一些， 上面系统压缩包还可以再解压，解压后如下：

    boot.img
    cache.img
    recovery.img
    system.img
    userdata.img

可以看到，里面还有很多东西，上面的flash-all.bat会简单粗暴的把所有文件都刷进去，但是有时候我们并不想这样，比如我想保留数据刷机，比如我的boot是加解密的，之前已经刷过，不需要再刷了比如我的recovery已经刷了第三方的了，不想刷回去。这时候就可以灵活掌握了。好了，现在已经基本分析完毕，下面讲解灵活刷机。

    刷机准备

    刷机
fastboot flash bootloader bootloader-shamu-moto-apq8084-71.10.img
fastboot reboot-bootloader
sleep 5
fastboot flash radio radio-shamu-d4.0-9625-02.101.img
fastboot reboot-bootloader
sleep 5
#fastboot -w update image-shamu-lmy48i.zip
# unzip image-shamu-lmy48i.zip
fastboot flash recovery recovery.img
fastboot reboot-bootloader
sleep 5
fastboot flash boot boot.img
fastboot reboot-bootloader
sleep 5
fastboot flash system system.img
fastboot reboot-bootloader
sleep 5
fastboot flash cache cache.img
fastboot flash userdata userdata.img

fastboot reboot


大功告成，以上各个步骤，根据需要自己选择。比如你系统挂掉了，你可以只刷系统，这样就保留数据系统还原。比如你只想刷第三方recovery，你就可以单刷recovery。比如系统升级了，但是你不想通过OTA升级，你就可以刷raido 刷bootloader，刷系统，保留你第三方的recovery和解加密的boot。总之，各部分功能都讲解了，大家根据需要自行刷机。


brightmoon ~ # adb devices
List of devices attached 
ZX1G22GPGW  device

brightmoon ~ # adb reboot bootloader
brightmoon ~ # adb devices
List of devices attached 

brightmoon ~ # adb devices
List of devices attached 

brightmoon ~ # fastboot devices
ZX1G22GPGW  fastboot
brightmoon ~ #      fastboot oem unlock
...
(bootloader) Please select 'YES' on screen if you want to continue...
(bootloader) Unlocking bootloader...
(bootloader) Unlock completed! Wait to reboot

OKAY [ 44.240s]
finished. total time: 44.240s


== ROOT & twrp ==
{{{
adb reboot bootloader
tools/fastboot-linux boot image/CF-Auto-Root-shamu-shamu-nexus6.img
adb reboot bootloader
fastboot flash recovery twrp-2.8.7.1-shamu.img 
}}}

http://www.ibtimes.co.uk/how-install-android-5-1-build-lmy47e-stock-firmware-nexus-6-1492430

# disable !
adb shell settings put global captive_portal_detection_enabled 0
# enable !
adb shell settings put global captive_portal_detection_enabled 1


# Factory Shamu images download
http://0s.mrsxmzlmn5ygk4tt.m5xw6z3mmuxgg33n.erenta.ru/android/nexus/images#shamu
https://dl.google.com/dl/android/aosp/shamu-lmy48m-factory-336efdae.tgz
http://forum.xda-developers.com/nexus-6/general/nightly-rom-stock-cm12-builds-t2995039
http://opengapps.org/
https://github.com/cgapps/vendor_google/tree/builds/arm
http://forum.xda-developers.com/nexus-6/development/rom-cleancore-vomer-100-lean-stock-03-t3059199

# LTE how to
http://bbs.gfan.com/android-7795111-1-1.html
