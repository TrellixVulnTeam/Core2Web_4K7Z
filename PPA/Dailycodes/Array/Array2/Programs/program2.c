#include<stdio.h>
void main(){
	int jerNo[]={18,7,45,12,10};
	float avg[]={49.90,54.30,45.50,47.54};
	int runs[5];
	
	printf("%ld\n",sizeof(jerNo));	//20
	printf("%ld\n",sizeof(avg));		//16
	printf("%ld\n",sizeof(runs));		//20
}

/*
	Sizeof  array is calculated as: No.of elements * sizeof datatype
	
	If we not specify any size to the array then it calculates using the no of elements present in a list.
	
	when we iniitialize array then according to the size of datatype space is given to the array. 
*/
