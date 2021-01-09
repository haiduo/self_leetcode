#include <iostream>
#include <unordered_map>
#include <climits> 
using namespace std;//https://leetcode-cn.com/problems/minimum-window-substring/solution/zui-xiao-fu-gai-zi-chuan-by-leetcode-solution/
class Solution {//未改进版的
public:
    unordered_map <char, int> ori, cnt;
    bool check() {
        for (const auto &p: ori) {
            if (cnt[p.first] < p.second) {
                return false;
            }
        }
        return true;
    }
    string minWindow(string s, string t) {
        for (const auto &c: t) {
            ++ori[c];
        }
        int l = 0, r = -1;
        int len = INT_MAX, ansL = -1, ansR = -1;
        while (r < int(s.size())) {
            if (ori.find(s[++r]) != ori.end()) {
                ++cnt[s[r]];
            }
            while (check() && l <= r) {
                if (r - l + 1 < len) {
                    len = r - l + 1;
                    ansL = l;
                }
                if (ori.find(s[l]) != ori.end()) {
                    --cnt[s[l]];
                }
                ++l;
            }
        }
        return ansL == -1 ? string() : s.substr(ansL, len);
    }
};

class Solution1 {

    unordered_map<char, int> need ;
    unordered_map<char, int> window;
public:
    string minWindow(string s, string t) {
        
        int tLen = t.length();//目标字符串
        int sLen = s.length();
        if(tLen == 0 || sLen==0) return "";

        //先把t中的字符放到need表中，计数
        for (int i = 0; i < tLen; i++) {
            char c = t[i];
            need.put(c, need.getOrDefault(c, 0) + 1);
        }

        int left = 0, right = 0;
        int len = Integer.MAX_VALUE, start = 0;
        int valid = 0; //已经匹配成功的字符种类数（非字符个数）

        //当右指针去到字符串末尾前
        while (right < sLen) {
            char c = s.charAt(right);
            right++;//右指针向右滑

            //如果右指针现在滑到的字符是目标字符串的一个，那么更新窗口中的数据
            if (need.containsKey(c)) {

                window.put(c, window.getOrDefault(c, 0) + 1);
                if(window.get(c).equals(need.get(c))){
                    valid++;
                }
            }
            
            //窗口开始从左边收缩
            while (valid == need.size() ) {
                if (right - left  < len) {
                    start = left;
                    len = right - left;
                }

                char d = s.charAt(left);
                left++;

                if (need.containsKey(d)) {
                    if(window.get(d).equals(need.get(d))){
                        valid--;
                    }
                    window.put(d, window.getOrDefault(d, 0) - 1);
                }
            }
        }
        return len == Integer.MAX_VALUE ? "" : s.substring(start, start + len);
    }
}
int main(){
	string s,t;
	cin>>s>>t;
    Solution so;
    s=so.minWindow(s,t);
	cout<<s<<endl;
    Solution1 so1;
    s=so1.minWindow(s,t);
    cout<<s<<endl;
	system("pause");
	return 0;
}