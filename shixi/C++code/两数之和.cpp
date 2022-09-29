#include <iostream>
#include <vector>
#include <unordered_map>
#include <ctime>
using namespace std;
class Solution {
    // 最简单的方法，就是从第一个数n1开始遍历，找到（target-n1）的数的下标;
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        // 返回数组，记录两个下标
        vector<int> res ;
        unordered_map<int, int> mymap;
        // 建立hash table array's value=> array's index
        for(int i=0; i<numbers.size(); i++){
            mymap[numbers[i]] = i;
        }
        // 第二次遍历，查询是否存在当前数的complement在hash table中
        for(int i=0; i<numbers.size(); i++){
            int complement = target - numbers[i];
            if(mymap.count(complement)!=0 && mymap.at(complement)!=i){
                res = {i+1, mymap.at(complement)+1};
                return res;
            }
        }
        throw invalid_argument("No two sum solution");
    }
};

int main(){
	Solution so;
    vector<int> numbers,res;
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
	res=so.twoSum(numbers,n);
    for(int i=0;i<res.size();i++)
    {
        cout<<res[i]<<" ";
    }
    cout<<endl;
	return 0;
}