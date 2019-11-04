//simple calculator	
#include<conio.h>
#include<iostream>
using namespace std;
int main()
{
	int ch;
	float a,b,c;
	cout<<"This program will help you to do simple calculations(addition/subtraction/multiplication/division)\n";
	cout<<"1	Addition\n2	Substraction\n3	Multiplication\n4	Division";
	cout<<"\nEnter your choice[1-4]: ";
	cin>>ch;
	cout<<"Enter a value ";
	cin>>a;
	cout<<"Enter another value";
	cin>>b;
	switch(ch)
	{
		case 1:c=a+b;
		cout<<"Sum of "<<a<<" and "<<b<<" is "<<c;break;
		case 2:c=a-b;
		cout<<"Difference between "<<a<<" and "<<b<<" is "<<c;break;
		case 3:c=a*b;
		cout<<"Multiplication of "<<a<<" and "<<b<<" is "<<c;break;
		case 4:c=a/b;
		cout<<"Division of "<<a<<" from "<<b<<" is "<<c;break;
		default:
			cout<<"you have entered a wrong choice";
	}
	return 0;
}
