= MPD play daemon =

== ncmpcpp ==
emerge mpd ncmpcpp

== configuration ==
sed '/^#/d;/^$/d' /etc/mpd.conf
{{{
music_directory                 "/mnt/play/MUSIC"
playlist_directory              "/var/lib/mpd/playlists"
db_file                 "/var/lib/mpd/database"
log_file                        "/var/lib/mpd/log"
pid_file                        "/var/lib/mpd/pid"
state_file                      "/var/lib/mpd/state"
user                            "mpd"
bind_to_address         "localhost"
bind_to_address         "/var/lib/mpd/socket"
auto_update     "yes"
follow_inside_symlinks          "yes"
input {
        plugin "curl"
}
filesystem_charset "UTF-8"
audio_output {    
        type            "httpd"
        name            "HTTP Stream"
        encoder         "vorbis"                # optional, vorbis(OGG) or lame(MP3)
        port            "8000"
        bitrate         "320"                   # do not define if quality is defined      
        format          "44100:16:1"
}
 
audio_output {
    type                    "fifo"
    name                    "my_fifo"
    path                    "/tmp/mpd.fifo"
    format                  "44100:16:2"
}
audio_output {
    type                    "alsa"
    name                    "My ALSA Device"
    device                  "hw:0,0"     # optional
}

}}}


== mpc ==
mpc update




https://wiki.gentoo.org/wiki/MPD

http://dotshare.it/category/mpd/ncmpcpp/

http://raspberrypi.stackexchange.com/questions/12339/pulseaudio-mpd-http-streaming-installation-guide
