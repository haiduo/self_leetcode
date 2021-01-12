#include <iostream>
#include <vector>
#include <ctime>
using namespace std;

int main(){
    vector<int> v;
	int n;
	cin>>n;
    srand( (unsigned)time(NULL) );// 设置种子
    for(int i=0;i<n;i++)
    {
        v.push_back(rand()%n);
    }
    for(int i=0;i<v.size();i++)
    {
        cout<<v[i]<<" ";
    }
    cout<<endl;
    int max=0;
    for(int i=0;i<v.size();i++)
    {
        if(v[i]>max){
            max=v[i];
        }
    }
    int a,b;
    a=max-v[0];
    b=max-v[v.size()-1];
    if(a>b){
        max=a;
    }
    else
    {
        max=b;
    }
    cout<<max<<endl;
	return 0;
}