#include <iostream>
using namespace std;

int main()
{
	int c, s=1; 
	cout<<"iput c( 0 < c <= 10000):";
	cin>>c;
	for(int i=2; i<=c/2; i++){
		if(c%i == 0) 
		   s += i;	
	}
	if(s == c && c!=1) 
		cout<<"It's a perfect number:"<<endl;
	else
		cout<<"Not a perfect number."<<endl;
	
	system("pause");
	return 0;
}
