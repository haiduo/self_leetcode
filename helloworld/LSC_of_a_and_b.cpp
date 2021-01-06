#include <iostream>
#include <string.h>
using namespace std;

int lcs(string a,string b,int len_a,int len_b);
int main()
{  
   string a = "program",b="algorithm";
   cout<<"LCS of a and b is "<<lcs(a, b, a.length()-1, b.length()-1)<<endl;
   system("pause");//getchar() in order to stop the screen after running
   return 0; 
}

int lcs(string a,string b,int len_a,int len_b)
   {
      if (len_a==-1 or len_b ==-1)
          return 0;
      else 
            if (a[len_a]==b[len_b])
          {
             return lcs(a,b,len_a-1,len_b-1) + 1;
          }
          else{
             return max(lcs(a,b,len_a-1,len_b),lcs(a,b,len_a,len_b-1));
          }
   }