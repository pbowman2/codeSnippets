# script for gathering data for threads
gcc -o matrixMult matrixMult.c -pthread
g++ -o doIOjobs doIOjobs.cpp -pthread

for i in 1 2 3 4 5 6 7 8 9 10
do
	echo "results for test $i" >> result.txt
	echo "time results for matrix multiplication" >> result.txt
	(time ./matrixMult 1500 1500 1500 1500 1) 2>> result.txt
	(time ./matrixMult 1500 1500 1500 1500 2) 2>> result.txt
	(time ./matrixMult 1500 1500 1500 1500 4) 2>> result.txt
	(time ./matrixMult 1500 1500 1500 1500 8) 2>> result.txt
	(time ./matrixMult 1500 1500 1500 1500 16) 2>> result.txt
	echo "time results for io jobs" >> result.txt
	(time ./doIOjobs 1) 2>> result.txt
	(time ./doIOjobs 2) 2>> result.txt
	(time ./doIOjobs 4) 2>> result.txt
	(time ./doIOjobs 8) 2>> result.txt
	(time ./doIOjobs 16) 2>> result.txt
done
echo "complete" >> result.txt
