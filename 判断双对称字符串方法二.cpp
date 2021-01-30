#include<bits/stdc++.h>
using namespace std;
 
string str;
 
bool Check( )
{
    string tmp = str;
    reverse( tmp.begin(), tmp.end() );
    return str == tmp;
}
 
int main()
{
    while( cin >> str )
    {
        int n = str.length();
        if( ( n & 1 ) || ( Check( ) == false ) )
        {
            cout << "false" << endl;
            continue;
        }
        string goal;
        goal.clear();
        int flag = 1;
        for( int i = 1; i < n; i += 2 )
        {
            if( str[ i ] != str[ i - 1 ] )
            {
                flag = 0;
                break;
            }
            goal += str[ i ];
        }
        if( flag ) cout << goal << endl;
        else       cout << "false" << endl;
    }
    return 0;
}
