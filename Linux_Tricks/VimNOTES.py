\section{}

|CTRL-L|      CTRL-L       Clear and redraw the screen.
|CTRL-G|      CTRL-G       show current file name (with path) and cursor position
|ga|   ga    show ascii value of character under cursor in decimal,hex,octal.
|g_CTRL-G|         g CTRL-G     show cursor column, line, and character position



|.|        N  .         repeat last change (with count replaced with N)
|q|           q         stop recording

|v_CTRL-V| CTRL-V       highlight blockwise or stop highlighting
|v_v|      v            highlight characters or stop highlighting
|M|        M            go to the middle line in the window, on the first

|x|     N  x            delete N characters under and after the cursor
|X|     N  X            delete N characters before the cursor

|e|     N  e            forward to the end of the Nth word
|ge|    N  ge           backward to the end of the Nth word
|w|     N  w            N words forward
|b|     N  b            N words backward

|n|     N  n            repeat last search
|N|     N  N            repeat last search, in opposite direction
|star|  N  *            search forward for the identifier under the cursor
|#|     N  #            search backward for the identifier under the cursor

|:marks|  :marks        print the active marks
|:ju|     :ju[mps]      print the jump list

|z.|               z.    or zz  redraw, current line at center of window


*Q_in*          Inserting text
|a|     N  a    append text after the cursor (N times)
|A|     N  A    append text at the end of the line (N times)
|i|     N  i    insert text before the cursor (N times) (also: <Insert>)
|I|     N  I    insert text before the first non-blank in the line (N times)


*Q_ss*          Special keys in Insert mode
|i_CTRL-W|      CTRL-W    delete word before the cursor
|i_CTRL-U|      CTRL-U    delete all entered characters in the current line
|i_CTRL-T|      CTRL-T    insert one shiftwidth of indent in front of current line
|i_CTRL-D|      CTRL-D    delete one shiftwidth of indent in front of current line

*Q_de*          Deleting text
|v_d|   {visual}d       delete the highlighted text

*Q_cm*          Copying and moving text
|yy|      N  yy         yank N lines into a register
|Y|       N  Y          yank N lines into a register
|p|       N  p          put a register after the cursor position (N times)
|P|       N  P          put a register before the cursor position (N times)

*Q_ch*          Changing text
|R|       N  R          enter Replace mode (repeat the entered text N times)
|r|       N  r{char}    replace N characters with {char}
|cc|      N  cc         change N lines

|gu|  gu{motion} make the text that is moved over with{motion}  lowercase
|gU|  gU{motion} make the text that is moved over with{motion}  uppercase

