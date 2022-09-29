/*
题目：工作分配（Workload）
设有n件工作分配给n个人。将工作i分配给第j个人所需的费用为cij。试设计一个算法，为每一个人都分配一件不同的工作，
并使总费用达到最小。设计一个算法，对于给定的工作费用，计算最佳工作分配方案，使总费用达到最小。
输入:
输入数据第一行有1个正整数n (1≤n≤20)。接下来的n行，每行n个数，第i行表示第i个人各项工作费用。
输出:
输出计算出的最小总费用。
样例输入:
3
4 2 5
2 3 6
3 4 5
样例输出:
9
*/
#include <iostream>
#include <vector>
using namespace std;

int n,cost=0;
int x[20],c[20][20];//x[20]下标表示第几列，内容为0表示这一列代表的工作还没有工人做

void workload(int i,int k){ //递归回溯（su）问题
      if (i==n && k < cost){
         cost = k;
         return ;
      }
      if (k<cost){
         for (int j =0; j< n; j++){
            if(x[j]==0){
               x[j]=1;
               workload(i+1,k +c[i][j]);
               x[j]=0;
            }
         }
      }
      return ;
}

int main()
{
   cout<<" workload distribution："<<endl;
   cin >> n;
   for (int i = 1; i <= n; i++){
      for (int j = 1; j <= n; j++){
         cin >> c[i][j];
         x[j] = 0; //先全部赋值为0  表示每一项工作都没有工人做过
      }
      cost += c[i][i]; //其实为感觉这个有点不合理  直接把cost=INT_MAX  int 类型里的最大值
   }
   workload(1, 0);
   cout << cost << endl;
   system("pause");
   return 0; 
}

