#!/usr/bin/perl
##
##
###############################################################################

use Getopt::Long;
GetOptions("n=i"=>\$strt, "c=s"=>\$tgtchn);

if ($#ARGV < 0) {
	print STDERR "usage: $0 <pdbfile>\n";
	exit -1;
}
my $pdbfile = $ARGV[0];
my $pdbfile_r = $pdbfile;

$pdbfile_r =~ s/\.pdb/_r.pdb/;

open (PDB, $pdbfile);
open (PDBR, ">$pdbfile_r") || die "cannot open $pdbfile_r";

my $innum  = -999;
my $in_ins  = ' ';
my $outnum = 0;
if (defined $strt) {
	$outnum = $strt-1;
}

while (my $line = <PDB>) {
	#if ($line =~ /^TER/) { $outnum=0; }

	if ($line !~ /^ATOM/) { next; }
	my $chnid = substr ($line, 21, 1);
	if (defined $tgtchn && $chnid ne $tgtchn) { next; }

	my $resid = substr ($line, 22, 4);
	my $inscode = substr ($line, 26, 1);
	if ($resid != $innum || $inscode ne $in_ins) {
		$innum = int($resid);
		$in_ins = $inscode;
		$outnum++;
	}

	substr ($line, 22, 4) = sprintf "%4d" , $outnum;
	print PDBR $line;
}
close (PDB);
close (PDBR);
