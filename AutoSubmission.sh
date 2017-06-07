for i in $( ls *minPBS ); 
do
	qsub $i
done
