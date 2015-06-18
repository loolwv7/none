cd .kodi/userdata
vi guisettings.xml 
{{{
<services>                                                                
        <airplay>true</airplay>                                              
        <airplaypassword></airplaypassword>                                  
        <devicename>Mediacenter</devicename>                                
        <esallinterfaces>true</esallinterfaces>                              
        <escontinuousdelay>25</escontinuousdelay>                            
        <esenabled>true</esenabled>                                          
        <esinitialdelay>750</esinitialdelay>                                  
        <esmaxclients>20</esmaxclients>                                      
        <esport>9777</esport>                                                
        <esportrange>10</esportrange>                                        
        <upnpannounce>true</upnpannounce>                                    
        <upnprenderer>true</upnprenderer>                                    
        <upnpserver>false</upnpserver>                                        
        <useairplaypassword>false</useairplaypassword>                        
        <webserver>true</webserver>                                          
        <webserverpassword>kodi</webserverpassword>                          
        <webserverport>80</webserverport>                                    
        <webserverusername>kodi</webserverusername>                          
        <webskin>webinterface.default</webskin>                              
        <zeroconf>true</zeroconf>                                            
</services> 
}}}


http://raspberrypi.stackexchange.com/questions/12671/how-to-enable-airplay-on-raspbmc-via-ssh

http://www.wexoo.net/20130330/changing-audio-and-other-settings-in-raspbmc
