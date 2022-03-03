#include <stdio.h>
int main() 
{
	//array declaration
	int rollNo[10];
	printf("Enter the roll numbers :\n")
	//taking inputs
	for(int i=0;i<10;i++)
	    scanf("%d",&rollNo[i]);
	
	//printing
	printf("The roll numbers are :\n")
	for(int i=0;i<10;i++)
	    printf("%d\n",rollNo[i]);
	return 0;
}


