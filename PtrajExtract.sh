for ((i=1; i<=25; i++));
do
l=`expr $i + $i - 1`
h=`expr $i + $i`

        echo "parm striga-5CBK-CLIM.prmtop"> cpptraj_$l.in
        echo "trajin 5CBK-CLIM-frame-$i-01.mdcrd">> cpptraj_$l.in
        echo "trajout 5CBK-CLIM-round3-frame-$l.rst restart onlyframes 5" >> cpptraj_$l.in
        echo "go">> cpptraj_$l.in
        echo "quit">> cpptraj_$l.in

        cpptraj -i cpptraj_$l.in

        echo "parm striga-5CBK-CLIM.prmtop"> cpptraj_$h.in
        echo "trajin 5CBK-CLIM-frame-$i-01.mdcrd">> cpptraj_$h.in
        echo "trajout 5CBK-CLIM-round3-frame-$h.rst restart onlyframes 500" >> cpptraj_$h.in
        echo "go">> cpptraj_$h.in
        echo "quit">> cpptraj_$h.in

        cpptraj -i cpptraj_$h.in

done
