#include<stdio.h>
#define L 10
void main(){
	auto money=10;
	switch(money,money*2){
		case L: printf("Willian");
			break;
			
		case L*2:printf("warren");
			break;
			
		case L*3:printf("Carlos");
			break;
			
		default:printf("Lawrence");
		
		case L*4:printf("Inqvar");
			break;
	}
}

/*
Output:
	Warren
-----------------------------------------------------------
Exp:
	The answer is Warren because condition in switch is commma separated
	and it is evaluated from right to left so case L*2  i.e 20 get 
	executed and also see here that L is not a variable here it a macro 
	which will be expanded in preprocessing stage as case only contains
	integer not variable name.
*/
