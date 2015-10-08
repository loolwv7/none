for upper in `find * -depth`; do (mv -f $upper `echo $upper | sed 's%[^/][^/]*$%%'``echo $upper | sed 's!.*/!!' | tr [:upper:] [:lower:]` 2>/dev/null); done
