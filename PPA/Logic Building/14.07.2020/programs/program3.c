//print sum of first 15 natural numbers

#include<stdio.h>
void main(){
	int sum=0;
	for(int i=1;i<=15;i++){
		sum=sum+i;
	}
	printf("sum=%d\n",sum);
}
