# http://media.io/progress.jsp;jsessionid=EF407A231E5569264265AD909CBF76A2
Trim or split videos with Mencoder

Mencoder makes it easy to trim the end or the beginning of a file, or split it in several parts.

Start from...

mencoder -ss 01:30:24 -oac copy -ovc copy in.avi -o out.avi

Replace 01:30:24 (1 hour, 30 minutes, 24 seconds) with the desired start time position.

End at...

mencoder -endpos hh:mm:ss -ovc copy -oac copy in.avi -o out.avi

Replace 00:45:00 (45 minutes) with the desired end position.

Split the movie

With the two commands above, you can for example split a movie in two bits:

mencoder -endpos 01:00:00 -ovc copy -oac copy movie.avi -o first_half.avi

mencoder -ss 01:00:00 -oac copy -ovc copy movie.avi -o second_half.avi

Replace 01:00:00 (1 hour) with the time when you want the split to occur. 

shnsplit -f The\ Dark\ Side\ Of\ The\ Moon.ape.cue -t"%n %p_%t" -o "flac flac -s  -8 -o %f -" The\ Dark\ Side\ Of\ The\ Moon.ape

ffmpeg -i xxx.mp4 -f mp3 -ab 192000 -vn music.mp3
