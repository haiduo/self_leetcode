#include <iostream>
#include<vector>
#include <climits>
using namespace std;
void maxAndSec(vector<int> &nums , int left , int right , int &Max , int &secMax)
    {
        if(left == right)
        {
            Max = nums[left];            
			secMax = INT_MIN;
            return;
        }
        if(left == right-1)
        {
             secMax = min(nums[right] , nums[left]);
             Max = max(nums[right] , nums[left]);
			 return;
        }
        int mid = (left + right)/2;
        int leftMax = 0 , leftSec = 0 ;
        maxAndSec(nums, left , mid , leftMax , leftSec);
        int rightMax = 0 , rightSec = 0;
        maxAndSec(nums , mid+1 , right , rightMax , rightSec);
        Max = max(leftMax , rightMax);
		if(leftMax < rightMax)
			secMax = max(leftMax , rightSec);
		else
			secMax = max(rightMax , leftSec);
    }
 
void maxAndSec2(int *nums , int len)
{
	if(len == 0)
		return ;
	int Max = nums[0];
	int secMax = INT_MIN;
	for(int i = 1 ; i < len ; i++)
	{
		if(nums[i] > Max)
		{
			secMax = Max;
			Max = nums[i];
		}
		else
		{
			if(nums[i] > secMax)
			{
				secMax = nums[i];
			}
		}
	}
	cout<<Max<<endl<<secMax<<endl;
}
int main()
{
	int num[7] = {2,4,3,5,6,7,3};
	maxAndSec2(num , 6);
	vector<int> nums(num , num+7);
	int max = 0 , secmax = 0 ;
	maxAndSec(nums,0,6,max,secmax);
	cout<<"最大值是："<<max<<endl<<"次大值是："<<secmax<<endl;
}
	