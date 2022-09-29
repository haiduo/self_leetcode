#include <iostream>
#include <iomanip>
using namespace std;

int main(int argc, char *argv[])
{
    int  x,n;
    cout<<"input number x (0<=x<=9) and high (n) of trapezoid (1<=n<=20) :"; 
    cin>>x>>n;
	cout<<endl;
	for(int j=0;j<3*n-2;j++) {
		if(j<(3*n-2)/2){
			cout<<setw(2)<<x;
			x++;
			x=x%10;
		}
        else{
			x=(x+10)%10;
			cout<<setw(2)<<x;
			x--;	
		}
	}
    cout<<endl;
	x++;
    for(int i=1;i<n-1;i++){
		x++;
		x=x%10;
        for(int j=1;j<i+1;j++) cout<<setw(2)<<' ';
        cout<<setw(2)<<x;
		for(int j=1;j<3*n-2*i-3;j++) cout <<setw(2)<<' ';
		cout<<setw(2)<<x;
        cout<<endl;
    }
	
	for(int j=0;j<n-1;j++) cout<<setw(2)<<' ';
	for(int j=0;j<n;j++) {
        if(j<n/2+1){
			x++;
			x=x%10;
			cout<<setw(2)<<x;
		}
        else{
			x--;
			x=(x+10)%10;
			cout<<setw(2)<<x;	
		}
	}
	cout<<endl;
    system("pause");
    return 0;
}


