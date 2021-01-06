#include <iostream>
#include <iomanip>
using namespace std;

int main(int argc, char *argv[])
{
    int  n;
	float sum=0;
    cout<<"input number (n) (1<=n<=100) :"; 
    cin>>n;
	for(int i=1;i<=n;i++) {
		sum+=1/float(i);		
	}
	cout<<"1+1/2+1/3+ ... +1/n=:"<<fixed << setprecision(6)<<sum;//保留小数点后面6位
	cout<<endl;
    system("pause");
    return 0;
}


