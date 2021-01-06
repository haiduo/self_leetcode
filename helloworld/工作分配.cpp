/*
题目：工作分配（Workload）
有n份工作要分配给n个人来完成，每个人完成一份。
第 i 个人完成第 k份工作所用的时间为一个正整数tik，
其中1 ≤ i, k ≤ n。试确定一个分配方案，使得完成这n份工作的时间总和最小。
*/
#include <iostream>
#include <string.h>
using namespace std;

void workload(int i,int k);
int main()
{  
   cout<<" workload distribution："<<endl;
   workload(5 ,5);
   system("pause");//getchar() in order to stop the screen after running
   return 0; 
}

void workload(int i,int k)
   { //回溯（su）问题
      if (i==N or k < cost){
         cost = k;
         return ;
      }
      if (k<cost){
         for (int j =0; j< N; j++){
            if(x[j]==0){
               x[j]=1;
               work(i+1,k +c[i][j]);
               x[j]=0;
            }
         }
      }
      return ;
   }