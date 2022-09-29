#include<stdio.h>  
// https://blog.csdn.net/hexmage/article/details/123886366
int main()  
{  
    int n,u,d;  
    scanf("%d%d%d",&n,&u,&d);   
    int t=(n-u)/(u-d);u-d;
    if(t*(u-d)<(n-u)) t++;  
    t*=2;
    t++;
    printf("%d\n",t);
    return 0;  
}
