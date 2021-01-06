#include <iostream>
using namespace std;

int num[15];

int write_in()
{
    char x;
    int i = 0;
    while(scanf("%c", &x) != EOF && x != '\n')
    {
        i++;
        if(x >= 'A' && x <= 'F'){
            num[i] = x - 'A' + 10;
        }
            
        else{
            if(x >= '0' && x <= '9'){
              num[i] = x - '0';
            }
            else {
                  return -1;         
            } 
        }           
    }
    return i;
}

int main(int argc, char *argv[])
{
    int digit = write_in();
    if(digit==-1){
       cout<<"input error!"<<endl; 
       system("pause");
       return 0;
    }
     else
     {
         int n = 0;
        for(int i = 0; i <= digit; ++i)
        {
            n = n * 16 + num[i];
        }
        cout << n << endl;
        system("pause");
        return 0;
     }  
}