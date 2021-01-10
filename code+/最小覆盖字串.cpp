#include <iostream>
#include <unordered_map>

using namespace std; //https://leetcode-cn.com/problems/minimum-window-substring/solution/zui-xiao-fu-gai-zi-chuan-by-leetcode-solution/
class Solution
{
public:
    unordered_map<char, int> ori, cnt;//构造两个分别叫ori(滑动窗口），cnt(字符串窗口)的哈希表，key为char，value为int，ori是被查字符串t的各字符数量
    
    bool check()
    {//检测函数，检测经过滑动划定的字符串是否全包含t的字符
        for (const auto& p : ori)
        {
            if (cnt[p.first] < p.second)
            {
                return false;
            }
        }
        return true;
    }
    string minWindow(string s, string t)
    {//未改进版的
        int sLen = s.length();
        int tLen = t.length();
        if (sLen == 0 || tLen == 0 || sLen < tLen)
            return "";
            
        for (const auto& c : t)     
            ++ori[c]; //确定t字符串各字符数量     
        /*
        定义左指l和右指r，为了能使字符串无论多长，在（r - l + 1 < len）第一次判断都能继续下去，
        将滑动确定的字符串长len初始指设为s的长度+1,ansL为最终字符串的左指。
        */
        int l = 0, r = -1;
        int len = s.length() + 1, ansL = -1, ansR = -1;
        
        while (r < int(s.size()))
        {
            if (ori.find(s[++r]) != ori.end())
            {//右指右移，如果字母是t中字母，cnt中的该字母数量加1
                ++cnt[s[r]];
            }
            /*
            当右移发现该字母不在t中，检测现在滑动确定的字符串是否全包含t，如果是在判断现在字符串是否为历次最短，
            如果是，则长度赋予len，左指赋予ansL
            */
            while (check() && l <= r)
            {
                if (r - l + 1 < len)
                {
                    len = r - l + 1;
                    ansL = l;
                }
                if (ori.find(s[l]) != ori.end())
                {
                    --cnt[s[l]];
                }
                ++l;//左指左移，如果是t中字符，减去cnt中该字符数量1
            }//此循坏直到滑动确定的字符串不满足check为止，再次开始右指右移
        }
        return ansL == -1 ? string() : s.substr(ansL, len);//判断最终字符串是否为空，然后输出结果
    }

    string minWindowPro(string s, string t)
    {//改进版 上面链接的视频讲解
        int sLen = s.length();
        int tLen = t.length();
        if (sLen == 0 || tLen == 0 || sLen < tLen)
            return "";
        //ascii('z') = 122
        int winFreq[128] = { 0 }, tFreq[128] = { 0 };//定义窗口字符频数数组和子串字符频数组数
        for (const auto& c : t) 
            tFreq[c]++;
       
        int distance = 0;//记录窗口字符数组内的非零值的频数之和，但下面总让其小于等于子串t的长度
        int minLen = sLen + 1;//初始化覆盖最小字符串的长度，为s的长度加1
        int begin = 0;//覆盖最小字符串的起点

        int left = 0;
        int right = 0;
        // [left,right)
        while (right < sLen)
        {
            //右边界扩张
            if (tFreq[s[right]] == 0) //右指针 直到遇到t内的字符，继续遍历，否则直接略过
            {
                right++;
                continue;
            }
            if (winFreq[s[right]] < tFreq[s[right]]) //检查当前字符在窗口数组的频数是否小于在子串字符组数的频数，考虑到窗口某个重复字符大于子串重复字符
                distance++;

            winFreq[s[right]]++; 
            right++;

            while (distance == tLen) //当长度相等，所对应的字符也就满足了
            {
                if (tFreq[s[left]] == 0) //做指针 直到遇到t内的字符，继续遍历，否则直接略过
                {
                    left++;
                    continue;
                }

                if (right - left < minLen)
                {
                    minLen = right - left;
                    begin = left;
                }            
                //左边界收缩
                if (winFreq[s[left]] == tFreq[s[left]])
                    distance--;

                winFreq[s[left]]--;
                left++;
            }
        }
        if (minLen == sLen + 1)
            return "";
        return s.substr(begin, minLen);//C++里的截取字符长度，s.substr(起点, 总长度)
    }
};

int main()
{
    string s, t, s1, s2;
    cin >> s >> t;
    t="";
    Solution so;
    s1 = so.minWindow(s, t);
    cout << s1 << endl;
    s2 = so.minWindowPro(s, t);
    cout << s2 << endl;
    system("pause");
    return 0;
}