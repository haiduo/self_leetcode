#include <iostream>
#include <string>
#include <vector>
#include <ctime>
#include <algorithm>

using namespace std;

class Solution
{
public:
	void maxHeapify(vector<int>& a, int i, int heapSize){
		int l=i*2+1,r=i*2+2,largest=i;
		if (l < heapSize && a[l]>a[largest]) largest =l;
		if (r < heapSize && a[r]>a[largest]) largest =r;
		if (largest !=i){
			swap(a[i],a[largest]);
			maxHeapify(a,largest,heapSize);//递归直到子堆都符合
		}
	}

	void buildMaxHeap(vector<int>& a,int heapSize){//自底向上，下滤依次建堆
		for (int i =(heapSize-1)/2;i>=0;--i){
			maxHeapify(a,i,heapSize);
		}
	}

	int findKthLargest(vector<int> &nums, int k)
	{
		int heapSize = nums.size();
		buildMaxHeap(nums,heapSize);
		for (int i=nums.size()-1; i >= nums.size()-k+1; --i){//自顶向下，下滤删除前k个，剩下的堆顶为结果
			swap(nums[0], nums[i]);
			--heapSize;
			maxHeapify(nums, 0 ,heapSize);
		}

		return nums[0];
	}
};

int main()
{
	int k, i = 0;
	cin >> k;
	vector<int> v;
	srand( (unsigned)time(NULL) );// 设置种子
	for(int i=0;i<10;i++) 
		v.push_back(rand()%50);
	for (int i = 0; i < v.size(); i++) 
		cout << v[i]<<" ";
	cout<<endl;
	Solution so;
	cout<<so.findKthLargest(v,k)<<endl;
	system("pause");
	return 0;
}
