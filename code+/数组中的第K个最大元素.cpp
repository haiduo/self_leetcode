#include <iostream>
#include <string>
#include <vector>
#include <ctime>
#include <algorithm>

using namespace std;

class Solution
{
public:
    //基于堆排序的选择方法 时间复杂度：O(nlogn) 空间复杂度：O(logn)，即递归使用栈空间的空间代价。
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

	int findKthLargestHeapSelect(vector<int> &nums, int k)
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

    //快速选择排序 时间复杂度：O(n) 空间复杂度：O(logn)
    int quickSelect(vector<int>& a, int l, int r, int index) {
        int q = randomPartition(a, l, r);
        if (q == index) {
            return a[q];
        } else {
            return q < index ? quickSelect(a, q + 1, r, index) : quickSelect(a, l, q - 1, index);
        }
    }

    inline int randomPartition(vector<int>& a, int l, int r) {
        int i = rand() % (r - l + 1) + l;
        swap(a[i], a[r]);
        return partition(a, l, r);
    }

    inline int partition(vector<int>& a, int l, int r) {
        int x = a[r], i = l - 1;
        for (int j = l; j < r; ++j) {
            if (a[j] <= x) {
                swap(a[++i], a[j]);
            }
        }
        swap(a[i + 1], a[r]);
        return i + 1;
    }

    int findKthLargestQuickSelect(vector<int>& nums, int k) {
        srand(time(0));
        return quickSelect(nums, 0, nums.size() - 1, nums.size() - k);
    }

};

int main()
{
	int k, i = 0;
	cin >> k;
	vector<int> v;
	srand( (unsigned)time(NULL) );// 设置种子
	for(int i=0;i<10;i++) 
		v.push_back(rand()%20);
	for (int i = 0; i < v.size(); i++) 
		cout << v[i]<<" ";
	cout<<endl;
	Solution so;
	cout<<so.findKthLargestHeapSelect(v,k)<<endl;
    cout<<so.findKthLargestQuickSelect(v,k)<<endl;
	system("pause");
	return 0;
}
