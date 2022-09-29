#include <iostream>
#include <vector>

using namespace std;
//https://leetcode-cn.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/solution/he-wei-k-de-zui-shao-fei-bo-na-qi-shu-zi-shu-mu-by/
class Solution {
public:
    int findMinFibonacciNumbers(int k) {//时间复杂度：O(44)。不超过 10^9的斐波那契数一共有 4444 个。空间复杂度：O(44)。
        int a = 1, b = 1;
        vector<int> fibo = {a, b};
        while (a + b <= k) {//迭代求解Fibo
            fibo.push_back(a + b);
            int c = a + b;
            a = b;
            b = c;
        }
        int ans = 0;
        for (int i = fibo.size() - 1; i >= 0; --i) {
            if (k >= fibo[i]) {//每次寻找k的次大值 
                ++ans;
				//cout<<fibo[i]<<endl;
                k -= fibo[i];
            }
        }
        return ans;
    }
};

int main(){
	Solution so;
	int k;
	cin>>k;
	cout<<so.findMinFibonacciNumbers(k)<<endl;
	return 0;
}