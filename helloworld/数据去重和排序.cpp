#include <iostream>
using namespace std;

void sort(int *a, int n);
void derepeat(int *a, int n);
int main()
{
	int n;
	cin >> n;
	int *a = new int[n]; //申请一个大小为n的数组，不要直接用int a[n];
	//因为数组大小必须是常数，这样做编译器不报错是因为编译器扩展
	for (int i = 0; i < n; ++i)
	{
		cin >> a[i];
	}
	sort(a, n);
	for (int i = 0; i < n; ++i)
	{
		cout << a[i] << " ";
	}
	cout << endl;
	derepeat(a, n);
	int i = 0;
	while (a[i])
	{
		cout << a[i++] << " ";
	}
	cout << endl;
	system("pause");
	return 0;
}

void sort(int *a, int n)
{
	int flag = 0, t;
	for (int i = 0; i < n; i++)
	{
		for (int j = 1; j < n - i; j++)
		{
			if (a[j - 1] > a[j])
			{
				flag = 1;
				t = a[j];
				a[j] = a[j - 1];
				a[j - 1] = t;
			}
		}
		if (flag == 0)
			break;
		else
			flag = 0;
	}
}
void derepeat(int *a, int n)
{
	int flag = 0, s = n;
	for (int i = 0; i < n; i++)
	{
		for (int j = i + 1; j < n; j++)
		{
			if (a[i] == a[j])
			{
				flag = 1;
				s--;
			}
			else
			{
				if (flag == 1)
				{
					for (int k = i + 1, h = j; h < n;)
					{
						a[k++] = a[h++];
					}
					flag = 0;
					break;
				}
				else
					break;
			}
		}
		n = s;
	}
	a[s] = '\0';
}
