$ENV{'TEXINPUTS'}='./style//:' . ($ENV{'TEXINPUTS'} // '');
$ENV{'BSTINPUTS'}='./style//:' . ($ENV{'BSTINPUTS'} // '');
$makeindex='makeindex -r -s style/svind.ist %O -o %D %S';
$pdf_mode=1;
$out_dir='build';
