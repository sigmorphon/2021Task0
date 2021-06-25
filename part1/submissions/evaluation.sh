langs=`ls ../ground-truth/`

for lan in $langs;
do
	echo $lan
	python evaluate.py --ref ../ground-truth/$lan --hyp guclasp/$lan

done
