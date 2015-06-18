== emerge xelatex ==
{{{
\documentclass[12pt,fleqn,titlepage,twoside,a4paper]{book}
\usepackage{etex}
\usepackage{amsfonts,amsmath,amssymb,graphicx}
\usepackage{txfonts}
\usepackage[centering,includeheadfoot,margin=1in]{geometry}
\usepackage{tabvar}
\usepackage{arabxetex}
%\newfontfamily{\arabicfont}[Script=Arabic,Scale=1.5]{Traditional Arabic}
 
\parindent = 0pt
 
\begin{document}
 
\begin{arab}[utf]
\chapter*{\textarab[utf]{ حِكَم من تَجمـيعي }}
\section*{\textarab[utf]{   شِعر    }}
 
  أديـن بدين الحـــب أنـى تــوجـهت ركـائبه \qquad فالحـــب دينــي و إيماني\\
 لنا أسوة في بشر هند و اختها و قيس و ليلى \qquad ثـــــم مـــــي و غـــيــــلان
\end{arab}
 
\end{document}
}}}
xelate test.tex

== add '~' accept_keywords ==
{{{
emerge -av dev-texlive/texlive-latexrecommended
}}}


http://www.heboliang.cn/archive/xetex-intro.html
