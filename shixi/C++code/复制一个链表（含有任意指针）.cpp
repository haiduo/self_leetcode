#include <iostream>
#include <unordered_map>
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

ListNode* copyListWithRand1(ListNode *head) {//哈希表方法
    unordered_map<ListNode*,ListNode*> map;
    ListNode * cur =head;
    while(cur!= NULL){
        ListNode *curnew = new ListNode ();
        curnew->value=cur->value;
        curnew->next = NULL;
        map[cur]=curnew;
        cur = cur ->next;
    }
    cur = head;
    while (cur != NULL) {//copy listnode
        map[cur]->next=map[cur->next];
        cur = cur->next;
    }
    return map[head];
}

int main(){
    ListNode *head = NULL;
    for (int i = 0; i < 10; i++)
        CreateList(head, i);
    printList(head);  
    head = copyListWithRand1(head);
    printList(head);
    system("pause");
    return 0;
}