#include <iostream>
#include <math.h>
using namespace std;

int main() {
    int n,sum=1,flag=1;
    cout<<"input a number(1<=n<=8000):";
    cin >> n;
    if (n == 1)
        cout <<"The biggest prime of the number:"<<1<< endl;
    else{
        while(n>1){
            for (int i = 2; i <= sqrt(n); i++){
                if(n%i==0) {
                    flag=0;
                    n--;
                    break;
                } 
            }
            if(flag==1) {
                break;
            }
            flag=1;
        }
        cout <<"The biggest prime of the number:"<<n<< endl;
    }
	system("pause");
    return 0;
}