#include<stdio.h>
void main(){
	int a=5,b=6,ans=0;
	
	ans=a++ + a++ + a++;
	printf("a=%d\tans=%d\t\n",a,ans);	//8 18
}
