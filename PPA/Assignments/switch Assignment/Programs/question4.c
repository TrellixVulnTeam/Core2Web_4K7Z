#include <stdio.h>
int main() {
	int x = 2;
	switch(x << (x + 1)) {
		default:
			printf("\ndefault");
		case 1:
			printf("\n1");
			break;
		case 2:
			printf("\n2");
			break;
		case 3:
			printf("\n3");
			break;
		case 4:
			printf("\n4");
			break;
		case 8:
			printf("\n8");
			break;
}
return 0;


/*
output:
	question4.c: In function ‘main’:
	question4.c:23:1: error: expected declaration or statement at end of input
	   23 | return 0;
	      | ^~~~~~
----------------------------------------------------------------------------------------
Exp:
	'}' is required at the end of return 0;
-------------------------------------------------------------------------------------------	
	
	
	      
*/
