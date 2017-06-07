c=0.15 # Desired Concentration
while read line
do

	echo "source leaprc.ff14SB"> tleap_${line}.in
	echo "loadamberparams frcmod.ionsjc_tip3p" >> tleap_${line}.in
	echo "complex=loadpdb ${line}.pdb">> tleap_${line}.in
	echo "solvatebox complex TIP3PBOX 10">> tleap_${line}.in
	echo "quit">> tleap_${line}.in
	
	tleap -f  tleap_${line}.in
	w=`grep "Added" leap.log | cut -c 9-13`
	a=`echo 0.018*$w |bc`
	n=`echo $a*$c |bc`
	echo "NUMBER!!!!"
	echo $n 
	N=$(round $n 0);
	echo $N
	cat > tleap_${line}.in << EOF
source leaprc.ff14SB 
loadamberparams frcmod.ionsjc_tip3p
complex=loadpdb ${line}.pdb
solvatebox complex TIP3PBOX 10
addions complex Na+ 0
addions complex Cl- 0
addions complex Na+ $N
addions complex Cl- $N
saveamberparm complex ${line}.prmtop ${line}.crd
savepdb complex ${line}_SetUp.pdb
quit
EOF
	tleap -f  tleap_${line}.in
done <strList


