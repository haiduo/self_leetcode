#include <iostream>
#include <unordered_map>
using namespace std;

//定义一个链表节点
struct ListNode{
    int value;
    ListNode *next;
};

static ListNode *tail = NULL;//记录最后一个结点

//插入一个新节点到链表中(放在链表头部)
void CreateList(ListNode *&head, int data){
    //创建新节点
    ListNode *p = (ListNode *)malloc(sizeof(ListNode));
    p->value = data;
    if(data == 0){
        tail = p;
    }
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

ListNode* getLoopNode(ListNode *head) {//哈希表方法
    if (head == NULL || head ->next == NULL || head->next->next == NULL){
        return NULL;
    }
    ListNode *n1 = head->next; // n1 -> slow
    ListNode *n2 = head->next->next; // n2 -> fast 
    while (n1 != n2) {
        if (n2->next == NULL || n2->next->next == NULL) {
            return NULL;
        }
        n2 = n2->next->next;
        n1 = n1->next;
    }
    n2 = head; // n2 -> walk again from head
    while (n1 != n2){
        n1 = n1->next;
        n2 = n2->next;
    }
    return n1;
}

int main(){
    ListNode *head = NULL , *p = NULL;
    for (int i = 0; i < 10; i++)
        CreateList(head, i);
    printList(head);
    cout << tail->value << endl;
    tail->next = head->next->next->next->next;
    p = getLoopNode(head);
    cout << p->value << endl;
    //printList(head); 死循环
    system("pause");
    return 0;
}