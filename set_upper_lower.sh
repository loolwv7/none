#! /bin/sh
# rename files to lower/upper case...
#
# usage:
#    move-to-lower *
#    move-to-upper *
# or
#    move-to-lower -R .
#    move-to-upper -R .
#

help()
{
cat << "EOF"
Usage: $0 [-n] [-r] [-h] files...
     -n      do nothing, only see what would be done
     -R      recursive (use find)
     -h      this message
     files   files to remap to lower case

     Examples:
            $0 -n *        (see if everything is ok, then...)
            $0 *

            $0 -R .

"EOF" 
}
 apply_cmd='sh'
     finder='echo "$@" | tr " " "\n"'
     files_only=

     while :
     do
         case "$1" in
             -n) apply_cmd='cat' ;;
             -R) finder='find "$@" -type f';;
             -h) help ; exit 1 ;;
             *) break ;;
         esac
         shift
     done

     if [ -z "$1" ]; then
             echo Usage: $0 [-h] [-n] [-r] files...
             exit 1
     fi

     LOWER='abcdefghijklmnopqrstuvwxyz'
     UPPER='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

     case `basename $0` in
             *upper*) TO=$UPPER; FROM=$LOWER ;;
             *)       FROM=$UPPER; TO=$LOWER ;;
     esac

     eval $finder | sed -n '
