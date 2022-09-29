#include <iostream>
#include <string.h>
#include <math.h>
using namespace std;

const double TINY_VALUE=1e-10;
double tsign(double x);
int main()
{  
	double x;
	cin>>x;
	cout<<"\n"<<tsign(x)<<endl;
	system("pause");
	return 0;
}

double tsign(double x) {
    //求sin(x)
	double g=0;
	double t =x;
	int n=1;
	do{
		g+=t;
		n++;
		t=-t*x*x/(2*n-1)/(2*n-2);
	} while (fabs(t)>=TINY_VALUE);
	return g;
}