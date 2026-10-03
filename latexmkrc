use Cwd qw(abs_path);
my $book_root = abs_path('.');
# Recent latexmk runs makeindex and BibTeX inside the output directory.
# Resolve paths at runtime so both old and new versions find the same assets.
$ENV{'TEXINPUTS'}="$book_root/style//:" . ($ENV{'TEXINPUTS'} // '');
$ENV{'BSTINPUTS'}="$book_root/style//:" . ($ENV{'BSTINPUTS'} // '');
$ENV{'BIBINPUTS'}="$book_root:" . ($ENV{'BIBINPUTS'} // '');
$makeindex='makeindex -r -s "' . $book_root . '/style/svind.ist" %O -o %D %S';
$pdf_mode=1;
$out_dir='build';
