#include <bits/stdc++.h>
using namespace std;
int main(){
    string s1, s2, min_str;
    // cin>>s1>>s2;
    s1 = "bachgbmcnuablc";
    s2 = "ablc";
    int n=s1.length(), m=s2.length(), l=0, r=0, Min=INT_MAX;
    unordered_map<int,int> M;
    if(n<m){
        puts("0");
        return 0;
    }
    for(int i=0;i<m;i++)
        M[s2[i]]++;
    for(int i=0,k=0;i<n;i++){
        M[s1[i]]--;
        if(M[s1[i]] >= 0){
            k++;
            if(k==m){
                while(M[s1[l]] < 0)
                    M[s1[l++]]++;
                if ((r-l+1) < Min){
                    Min = (r-l+1);
                    min_str = s1.substr(l, Min);
                }
                M[s1[l++]]++;
                k--;
            }
        }
        r++;
    }
    cout<<min_str;
    return 0;
}