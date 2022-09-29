/*

*/
#include <iostream>
#include <string.h>

using namespace std;

void ox(int n);

int main()
{
   int n;
   cout<<"input intance number:";
   cin >> n ;
   cout<<endl;
   ox(n);
   system("pause");
   return 0;
}

void ox(int n)
{
    int a=n, w[20], digi = 0;
    char arr[]={'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
    cout<<"output settle:";
    while(a)
    {
        w[digi] = a % 16; // 用数组w来记录每次得到的商
        digi++;
        a = a / 16;
    }
    for(int j = digi - 1; j >= 0; j--)
    {
       /*
        if(w[j] >= 10)
            cout << char('A' + w[j] - 10); // 把大于9的数转化为16进制的字母
        else
            cout << w[j]; 
      */
     cout << arr[w[j]];
    }
   cout<<endl;
}