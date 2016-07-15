= Docker How To =

docker run -t -i centos /bin/bash


Hi, Brian,

 

 This seems to be an issue related to Docker running out of disk space. A few
 general solutions which seem to work for others include simply waiting and
 retrying to pull the image, removing the contents of your /var/lib/docker
 directory and restarting your Docker instance (be sure to save anything
         crucial first!), or setting DOCKER_STORAGE_OPTIONS in
 /etc/sysconfig/docker-storage to an empty value.

  

  If these don't work for your instance, you may want to take a look at the
  contents of /var/lib/docker/devicemapper/devicemapper/metadata; see if there
  are any apparent errors, and if so we can address them more directly.

   

   As the NameError you're seeing near the bottom, that's an issue with the
   install file that has since been resolved - replacing your version of
   step1_ecs_singlenode_install.py with the most recent version should prevent
   the error in the future.

    
docker ps
docker exec -it zabbix bash
