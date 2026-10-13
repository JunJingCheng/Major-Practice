% !Mode:: "TeX:UTF-8"
\NeedsTeXFormat{LaTeX2e}[1999/12/01]
\ProvidesClass{hquthesis}[2022/01/11 1.0 Huaqiao University Thesis Template for Bachelor Degree]

\LoadClass[zihao=-4,a4paper,oneside]{ctexbook}
%采用A4纸张、文本正文（宋体、小四号）
\setmainfont{Times New Roman}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{ctexbook}}
%---------------打印设置-------------------------------------
\ProcessOptions
\newif\ifprint\printfalse
\DeclareOption{forprint}{\printtrue}
\ProcessOptions



%%-------------------页面布局-------------------------- 
\RequirePackage{fancyhdr,hyperref}

\hypersetup{pdfencoding=auto}  
 \ifprint
 \hypersetup{hidelinks}
 \else
\hypersetup{citecolor=magenta,linkcolor=blue}
\fi
\RequirePackage[top=3.0truecm,bottom=2.5truecm,left=3truecm,right=2.5truecm,includefoot,xetex]{geometry}    % 页面设置

\newtoks\major             %学科专业中文名
\newtoks\advisor           %指导教师中文名
\newtoks\schoolname        %学院中文名
\newtoks\grade             %界别
\newtoks\studentnumber     %学号
\newtoks\professionaltitle %职称
\newtoks\cntitle           %中文标题
\newtoks\entitle           %英文标题
\pagestyle{fancyplain}
\fancyhf{}  %清除以前对页眉页脚的设置
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[C]{-\,\thepage\,-}

\fancypagestyle{plain}
{
\fancyhead{}                                    
\renewcommand{\headrulewidth}{0pt}
\fancyfoot{}                                    
\fancyfoot[C]{-\,\thepage\,-}
}
\usepackage{ulem}
\newcommand\dlmu[2][4cm]{\hskip1pt\underline{\hb@xt@ #1{\hss#2\hss}}\hskip3pt}
%%-------------------封面----------------------------- 
\RequirePackage{multirow}
\def\maketitle{
  %\null
  \thispagestyle{empty}
\begin{figure}
	\centering
	\includegraphics[width=0.5\linewidth]{figures/huada_title}
	\label{fig:huadatitle}
\end{figure}
  \begin{center}\leavevmode%标题在一行
 \begin{center}
 	   {\heiti\zihao{0} {毕业实训}}\\
    \vspace{1.2cm}	% original: 1.8cm

{\zihao{3}\begin{tabular}{rc}
		\heiti\zihao{3}{题目：} & \multirow[t]{2}{350pt}{\centering{\the\cntitle}} \\ 
		\cline{2-2} & \\
		\cline{2-2} & \\
\end{tabular}}
    \vspace{0.2cm}	% original: 0.9cm
 \end{center}

    {\zihao{-3}
    \begin{tabular}{cp{4cm}c}
    	
    	
    	\heiti\raisebox{-2ex}[0pt]{\makebox[3.5cm][s]{学\hfill 院：}} & \songti{  {}\raisebox{-2ex}[0pt]{\the\schoolname}\hfill{}} & \\
    	
    	\heiti\raisebox{-2ex}[0pt]{\makebox[3.5cm][s]{专\hfill 业：}} & \songti{ {}\raisebox{-2ex}[0pt]{\the\major}\hfill{}} & \\
    	
    	\heiti\raisebox{-2ex}[0pt]{\makebox[3.50cm][s]{届\hfill 别：}} & \songti{ {}\raisebox{-2ex}[0pt]{\the\grade}\hfill{}} & \\
    	
    	\heiti\raisebox{-2ex}[0pt]{\makebox[3.5cm][s]{学\hfill 号：}} & \songti{ {}\raisebox{-2ex}[0pt]{\the\studentnumber}\hfill{}} & \\
    	
    	\heiti\raisebox{-2ex}[0pt]{\makebox[3.5cm][s]{姓\hfill 名：}} & \songti{ {}\raisebox{-2ex}[0pt]{\@author}\hfill{}} & \\
    	
    	\heiti\raisebox{-2ex}[0pt]{\makebox[3.5cm][s]{指\hfill 导\hfill 老\hfill 师：}} & \songti{ {}\raisebox{-2ex}[0pt]{\the\advisor}\hfill{}} & \\
    	
    	\heiti\raisebox{-2ex}[0pt]{\makebox[3.5cm][s]{指\hfill 导\hfill 老\hfill 师\hfill 职\hfill 称：}} & \songti{ {}\raisebox{-2ex}[0pt]{\the\professionaltitle}\hfill{}} & \\
    \end{tabular}
    }
\vspace{0.3cm}	% original: 0.8cm

%\begin{center}
%	{\heiti\zihao{4} {华侨大学教务处印制}}\\
%{\heiti\zihao{4} {\@date}}
%\end{center}
    \par
    \vspace{2cm}	% original: 2.6cm
  \end{center}%
  }


%-----------------摘要和关键词 -------------------------
%中英文摘要（宋体、五号）
%关键词（宋体、五号，不超过五个）
\newcommand\cnabstractname{摘要} 
\newcommand\enabstractname{ABSTRACT}
\newcommand\cnkeywords[1]{ {\noindent\heiti\zihao{-4}\cnkeywordsname: }#1}
\newcommand\cnkeywordsname{关键词}
\newcommand\enkeywords[1]{ {\noindent\bfseries\zihao{-4}\enkeywordsname: }#1}
\newcommand\enkeywordsname{Key words}

\newenvironment{cnabstract}{
    \newpage
     \begin{center}
     	{\heiti\zihao{3} {\the\cntitle}}
     \end{center}
 
\vspace{80pt}

\begin{center}
	{\heiti\zihao{4} {摘要}}
\end{center}
    \@afterheading}
    {\par}

\newenvironment{enabstract}{
    \newpage
    \begin{center}
    	{\heiti\zihao{3} {\the\entitle}}
    \end{center}
    \vspace{40pt}
    
    \begin{center}
    	{\heiti\zihao{4} {Abstract}}
    \end{center}
    \@afterheading}
    {\par}

%%----------------常用宏包----------------------------- 
\RequirePackage{amsmath,amssymb}
\RequirePackage[amsmath,thmmarks]{ntheorem}% AMSLaTeX宏包.
\RequirePackage{graphicx}                 % 图形
\RequirePackage{color,xcolor}             %支持彩色
%\RequirePackage{mathrsfs}   % 不同于\mathcal or \mathfrak 之类的英文花体字体
\RequirePackage{url}
\RequirePackage{enumerate}
\RequirePackage{hyperref} 
\RequirePackage{cases}
\RequirePackage{longtable}
\RequirePackage{ulem}
\RequirePackage{mathtools}
\RequirePackage[linesnumbered,ruled,vlined]{algorithm2e}

\usepackage{latexsym}


\usepackage{longtable}
	\setlength{\LTleft}{0pt} \setlength{\LTright}{0pt} %表格与页面左右边缘之间的矩离均为０
%%---------------定理类环境定义------------------------- 
\theoremstyle{plain}
\theoremheaderfont{\heiti}
\theorembodyfont{\songti} \theoremindent0em
\theorempreskip{0pt}
\theorempostskip{0pt}
\theoremnumbering{arabic}
%\theoremsymbol{} %定理结束时自动添加的标志
\newtheorem{theorem}{\hspace{2em}定理}[section]
\newtheorem{definition}{\hspace{2em}定义}[section]
\newtheorem{lemma}{\hspace{2em}引理}[section]
\newtheorem{corollary}{\hspace{2em}推论}[section]
\newtheorem{proposition}{\hspace{2em}性质}[section]
\newtheorem{example}{\hspace{2em}例}[section]
\newtheorem{remark}{\hspace{2em}注解}[section]
%\newtheorem{algorithm}{\hspace{2em}算法}[section]
\newtheorem{axiom}{\hspace{2em}公理}[section]
\newtheorem{condition}{\hspace{2em}条件}[section]
\newtheorem{conclusion}{\hspace{2em}结论}[section]
\newtheorem{assumption}{\hspace{2em}假设}[section]

\theoremstyle{nonumberplain}
\theoremheaderfont{\heiti}
\theorembodyfont{\normalfont \rm \songti}
\theoremindent0em \theoremseparator{\hspace{1em}}
\theoremsymbol{$\square$}
\newtheorem{proof}{\hspace{2em}证明}

%%---------------------引用格式------------------------ 
\newcommand{\upcite}[1]{\textsuperscript{\cite{#1}}}  %自定义新命令\upcite, 使参考文献引用以上标出现

\makeatletter \setlength\partopsep{0pt}
\def\@listI{\leftmargin\leftmargini
            \parsep 0pt
            \topsep \parsep
            \itemsep \parsep}
\def\@listii {\leftmargin\leftmarginii
              \labelwidth\leftmarginii
              \advance\labelwidth-\labelsep
              \parsep    \z@ \@plus\z@  \@minus\z@
              \topsep    \parsep
              \itemsep   \parsep}
\def\@listiii{\leftmargin\leftmarginiii
              \labelwidth\leftmarginiii
              \advance\labelwidth-\labelsep
              \parsep    \z@ \@plus\z@  \@minus\z@
              \topsep    \parsep
              \itemsep   \parsep}
\def\@listiv{\leftmargin\leftmarginiv
              \labelwidth\leftmarginiv
              \advance\labelwidth-\labelsep
              \parsep    \z@ \@plus\z@  \@minus\z@
              \topsep    \parsep
              \itemsep   \parsep}
\def\@listv{\leftmargin\leftmarginv
              \labelwidth\leftmarginv
              \advance\labelwidth-\labelsep
              \parsep    \z@ \@plus\z@  \@minus\z@
              \topsep    \parsep
              \itemsep   \parsep}
\def\@listvi{\leftmargin\leftmarginvi
              \labelwidth\leftmarginvi
              \advance\labelwidth-\labelsep
              \parsep    \z@ \@plus\z@  \@minus\z@
              \topsep    \parsep
              \itemsep   \parsep}

%%-------------更改列表环境的边距------------------------

\setlength\leftmargini   {2\ccwd} \setlength\leftmarginii  {\leftmargini} 
\setlength\leftmarginiii {\leftmargini}
\setlength\leftmarginiv  {\leftmargini} \setlength\leftmarginv   {\ccwd} \setlength\leftmarginvi  {\ccwd} 
\setlength\leftmargin    {\leftmargini} 
\setlength\labelsep      {.5\ccwd}
\setlength\labelwidth    {\leftmargini}
\setlength\listparindent{2\ccwd}
%把列表中缩进改为2\ccwd（当前汉字字号宽）
\def\list#1#2{\ifnum \@listdepth >5\relax \@toodeep
     \else \global\advance\@listdepth\@ne \fi
  \rightmargin \z@ \listparindent2\ccwd \itemindent \z@
  \csname @list\romannumeral\the\@listdepth\endcsname
  \def\@itemlabel{#1}\let\makelabel\@mklab \@nmbrlistfalse #2\relax
  \@trivlist
  \parskip\parsep \parindent\listparindent
  \advance\linewidth -\rightmargin \advance\linewidth -\leftmargin
  \advance\@totalleftmargin \leftmargin
  \parshape \@ne \@totalleftmargin \linewidth
  \ignorespaces}

\makeatother
%%-----------------致谢设置---------------------------- 
\newcommand\acknowledgement{\chapter*{\ziju{2}致谢}}

%%---------------章节标题设置 --------------------------
%标题（宋体、三号）
\ctexset{chapter={format+={\zihao{3}},%
               number={\zihao{3}\arabic{chapter}},name={,},afterskip={30pt},beforeskip={20pt}}}
\ctexset{section={format+={\zihao{4}\raggedright}}}
\ctexset{subsection={format+={\zihao{-4}\raggedright}}}
\ctexset{subsubsection={format={\zihao{-4}\bf\raggedright}}}

\setcounter{tocdepth}{4}
\setcounter{secnumdepth}{4}

%%---------------图表标题设置--------------------------- 
\RequirePackage[labelsep=quad]{caption} %% 序号之后空一格写标题
%\captionsetup[table]{textfont=bf}  %%设置表格标题字体为黑体
\renewcommand\figurename{\zihao{5} 图}
\renewcommand\tablename{\zihao{5} 表} 

%%---------------目录设置------------------------------ 
%目录（宋体、小四号）
\ctexset{contentsname={目\qquad 录}}
\RequirePackage{tocloft} 
\renewcommand\cftchapfont{\bf\zihao{-4}}
\renewcommand\cfttoctitlefont{\hfill\zihao{-2}\bf}
\renewcommand\cftaftertoctitle{\hfill}
\usepackage{titletoc}


%%---------------参考文献------------------------------
%\usepackage{natbib}
%\bibliographystyle{plain} 
%\bibliographystyle{xiaoxv} 
%\bibliographystyle{hquthesis-bib-style} 
  %参考文献样式 plain,unsrt,alpha，abbrv，ieeetr，acm，siam，apalike等
%\bibliographystyle{GB/T 7714-2005}


\graphicspath{{figures/}}        % 图片文件路径

\allowdisplaybreaks

\endinput
