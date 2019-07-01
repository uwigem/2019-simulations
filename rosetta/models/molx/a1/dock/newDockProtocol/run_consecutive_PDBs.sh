for i in 3 4 5 6 7 8 9
do 
	let j=$i-1;
	sed -i "s/MOL_0X/MOL_0$i/g" run_ligdock.sh;
	./run_ligdock.sh;
	sed -i "s/MOL_0$i/MOL_0X/g" run_ligdock.sh;
done
