#include<stdio.h>
void main(){
	int x,y,z;
	printf("Enter three values\n");
	scanf("%d %d %d",&x, &y,&z);
	
	if(x>y){
		if(x>z){
			printf("%d is greater\n",x);
		}else{
			printf("%d is greater\n",z);
		}
	}else{
		if(y>z){
			printf("%d is greater\n",y);
		}else{
			printf("%d is greater\n",z);
		}
	}
	
}
