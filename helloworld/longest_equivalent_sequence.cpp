#include <iostream>
#include <math.h>
using namespace std;

int main() {
    int n,s=0,e=0,s1=0,e1=0,sub_max=0,max=0;
    cout<<"input a number(1<n<=50):";
    cin >> n;
    cout<<"input a digital list:";
    int a[n+1];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    a[n]=-1;
    for(int i=1;i<n+1;i++){
        if(a[s1]==a[i]){
          sub_max++;
        }
        else{
            e1=i-1;
            if(sub_max>max){
                max=sub_max;
                s=s1;
                e=e1;
            }
            s1=i;
            sub_max=0;
        }
    }
    if(max<1){
        cout<<"No answer!"<<endl;
    }    
    else
    {
        cout <<"The strt and end of the biggest sublist:"<<s<<" "<<e<< endl;

    }
    
	system("pause");
    return 0;
}