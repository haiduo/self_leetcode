#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main()
{
    int n;
	cin >> n;
	int* a = new int[n];//申请一个大小为n的数组，不要直接用int a[n];
	//因为数组大小必须是常数，这样做编译器不报错是因为编译器扩展 
	for(int i=0; i<n; ++i){
		cin >> a[i];
	} 
	int start=0, end=0, max_num=1;//记录相等序列起始位置、末尾位置、最长序列长度 
	for(int i=0; i<n; ++i){
		int cnt = 1;//记录相等序列长度 
		for(int j=i+1; j<n; ++j){
			if(a[i]==a[j]){
				++cnt;
			}
			else{
				break;
			} 
			if(cnt>max_num){
                    max_num = cnt;//更新最大序列长度 
                    start = i;
                    end = j;
                    i=j-1;
                } 
		}
	}
	if(max_num==1){
		cout << "No answer." << endl;
	}
	else{
		cout << start << ' ' << end << endl;
	}
    system("pause");
    return 0;
}
