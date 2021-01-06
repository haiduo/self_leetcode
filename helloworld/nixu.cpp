// test.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream> 
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
int n = 0;//全局变量，用于统计逆序对数  
void merge(int a[], int first, int mid, int last)
{
	int* temp = new int[last - first + 1];//临时数组，用于临时存放比较后的数字  
	int i = first, j = mid + 1, k = 0;
	while (i <= mid && j <= last)//遍历比较左右两个部分  
	{
		if (a[i] <= a[j])
			temp[k++] = a[i++]; //左半部分元素小于右半部分的元素，将左边该元素存入临时数组  
		else
		{
			temp[k++] = a[j++];
			n = n + (mid - i + 1);//统计左半边能和右半边该元素构成的逆序对数  
		}
	}
	while (i <= mid)
		temp[k++] = a[i++];
	while (j <= last)
		temp[k++] = a[j++];
	for (i = 0; i < k; i++)
		a[first + i] = temp[i];//从临时数组取出放回原数组  
}
void mergesort(int a[], int first, int last)
{
	if (first < last)
	{
		int mid = (first + last) / 2;
		mergesort(a, first, mid);//递归排序左半部分  
		mergesort(a, mid + 1, last);//递归排序右半部分  
		merge(a, first, mid, last);//将处理后的两个部分合并  
	}
}

int main()
{
	int a[6] = { 6,5,4,3,2,1 }, i;
	cout << "序列:";
	for (i = 0; i < 6; i++)
		cout << a[i] << " ";
	cout << endl;
	mergesort(a, 0, 5);
	cout << endl << "逆序对数：" << n << endl;
	return 0;
}
// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单

// 入门使用技巧: 
//   1. 使用解决方案资源管理器窗口添加/管理文件
//   2. 使用团队资源管理器窗口连接到源代码管理
//   3. 使用输出窗口查看生成输出和其他消息
//   4. 使用错误列表窗口查看错误
//   5. 转到“项目”>“添加新项”以创建新的代码文件，或转到“项目”>“添加现有项”以将现有代码文件添加到项目
//   6. 将来，若要再次打开此项目，请转到“文件”>“打开”>“项目”并选择 .sln 文件
