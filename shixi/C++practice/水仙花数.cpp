#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	int c,t, s=0; 
	cout<<"iput c( 0 < c <= 10000):";
	cin>>c;
	t=c;
	do{
		s=pow(c%10,3)+s;
	}
	while (c=c/10);
	
	if(s==t) cout<<"it is a narcissistic number."<<endl;
	else cout<<"Not a narcissistic number."<<endl;
	
	system("pause");
	return 0;
}
