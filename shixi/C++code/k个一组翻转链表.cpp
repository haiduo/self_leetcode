#include <iostream>
using namespace std;

//定义一个链表节点
struct ListNode{
    int value;
    ListNode *next;
};

//插入一个新节点到链表中(放在链表头部)
void CreateList(ListNode *&head, int data){
    //创建新节点
    ListNode *p = (ListNode *)malloc(sizeof(ListNode));
    p->value = data;
    p->next = NULL;

    if (head == NULL){
        head = p;
        return;
    }
    p->next = head;
    head = p;
}

void printList(ListNode *head){
    ListNode *p = head;
    while (p != NULL){
        cout << p->value << " ";
        p = p->next;
    }
    cout << endl;
}

class Solution {
public:
    // 翻转一个子链表，并且返回新的头与尾
    pair<ListNode*, ListNode*> myReverse(ListNode* head, ListNode* tail) {
        ListNode* prev = tail->next;
        ListNode* p = head;
        while (prev != tail) {
            ListNode* nex = p->next;
            p->next = prev;
            prev = p;
            p = nex;
        }
        return {tail, head};
    }

    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* hair;
        hair->next = head;
        ListNode* pre = hair;

        while (head) {
            ListNode* tail = pre;
            // 查看剩余部分长度是否大于等于 k
            for (int i = 0; i < k; ++i) {
                tail = tail->next;
                if (!tail) {
                    return hair->next;
                }
            }
            ListNode* nex = tail->next;
            // 这里是 C++11 的写法
            pair<ListNode*, ListNode*> result = myReverse(head, tail);
            head = result.first;
            tail = result.second;
            // 这里是 C++17 的写法
            //tie(head, tail) = myReverse(head, tail);
            // 把子链表重新接回原链表
            pre->next = head;
            tail->next = nex;
            pre = tail;
            head = tail->next;
        }

        return hair->next;
    }
};


int main(){
    ListNode *head = NULL;
    for (int i = 15; i >= 1; i--)
        CreateList(head, i);
    printList(head);
    int k;
    cin>>k;
    Solution so;
    head=so.reverseKGroup(head,k);
    printList(head);

    system("pause");
    return 0;
}