#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	int c; 
	cout<<"iput c( 0 < c <= 10000):";
	cin>>c;

	long a = 0, b = sqrt(c);
	while (a <= b) {
		if (a * a + b * b == c) {
			cout<<"It's a perfect number:"<<endl;
			system("pause");
			return 0;
		}
		
		else {
			if (a * a + b * b < c)  ++a;
		    else  --b;
		}
	}
	cout<<"Not a perfect number."<<endl;
	
	system("pause");
	return 0;
}
