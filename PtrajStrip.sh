for ((i=1; i<=25; i++));
do


        echo "parm 5CBK.prmtop"> cpptraj_strip_$i.in
        echo "trajin 5CBK-CLIM-frame-$i-01.mdcrd">> cpptraj_strip_$i.in
	echo "autoimage">> cpptraj_strip_$i.in
	echo "strip :WAT">> cpptraj_strip_$i.in
	echo "strip :Cl-">> cpptraj_strip_$i.in
	echo "strip :Na+">> cpptraj_strip_$i.in
        echo "trajout 5CBK-CLIM-round3-frame-$l.mdcrd" >> cpptraj_strip_$i.in
        echo "go">> cpptraj_strip_$i.in
        echo "quit">> cpptraj_strip_$i.in

        cpptraj -i cpptraj_strip_$i.in

done
