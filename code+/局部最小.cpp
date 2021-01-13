#include <iostream>
#include <vector>
#include <ctime>
using namespace std;

class Solution{
public:
    int getLessIndex(vector<int> &arr){
        if (arr.size() == 0){
            return -1;//no exist
        }
        if (arr.size() == 1 || arr[0] < arr[1]){
            return 0;
        }
        if (arr[arr.size()-1] < arr[arr.size()-2]){
            return arr.size()-1;
        }
        int left = 1;
        int right = arr.size()-2;
        int mid = 0;
        while (left < right){
            mid = (left + right) /2;
            if (arr[mid] > arr[mid - 1]) {
                right = mid -1;
            }else if (arr[mid] > arr[mid + 1]){
                left = mid + 1;
            }else{
                return mid;
            }
        }
        return left;
    }
}; 

int main(){
    Solution so;
    vector<int> numbers;
	int n;
	cin>>n;
    srand( (unsigned)time(NULL) );// 设置种子
    for(int i=0;i<n;i++)
    {
        numbers.push_back(rand()%n);
    }
    for(int i=0;i<numbers.size();i++)
    {
        cout<<numbers[i]<<" ";
    }
    cout<<endl;
	cout<<so.getLessIndex(numbers)<<endl;
    system("pause");
	return 0;
}