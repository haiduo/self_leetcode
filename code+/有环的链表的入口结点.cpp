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

ListNode* getLoopNode(ListNode *head) {//快慢指针方法 单链表的有环入口节点
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

ListNode* noLoop(ListNode *head1, ListNode *head2) {//两个链表相交到某一个节点
    if (head1 == NULL || head2 == NULL) {
        return NULL;
    }
    ListNode* cur1 = head1;
    ListNode* cur2 = head2;
    int n = 0;
    while (cur1->next != NULL){
        n++;
        cur1 = cur1->next;
    }
    while ( cur2->next != NULL){
        n--;
        cur2 = cur2->next;
    }
    if (cur1 != cur2)
    {
        return NULL;
    }
    //n:链表1长度减去链表2的长度
    cur1 = n > 0 ? head1 : head2;//谁长，谁的头变成cur1
    cur2 = cur1 == head1 ? head2 : head1;//谁短，谁的头变成cur2
    n = abs(n);
    while (n != 0)
    {
        n--;
        cur1 = cur1->next;
    }
    while (cur1 != cur2)
    {
        cur1 = cur1->next;
        cur2 = cur2->next;
    }
    return cur1;
}

//两个有环链表，返回第一个相交节点，如果不相交返回NULL 三种情况
ListNode* bothLoop(ListNode *head1,ListNode *loop1,ListNode *head2, ListNode *loop2) {
    ListNode *cur1 = NULL;
    ListNode *cur2 = NULL;
    if (loop1 == loop2) {       
        cur1 = head1;
        cur2 = head2;
        int n = 0;
        while (cur1 != loop1){
            n++;
            cur1 = cur1->next;
        }
        while ( cur2 != loop2){
            n--;
            cur2 = cur2->next;
        }
        //n:链表1长度减去链表2的长度
        cur1 = n > 0 ? head1 : head2;//谁长，谁的头变成cur1
        cur2 = cur1 == head1 ? head2 : head1;//谁短，谁的头变成cur2
        n = abs(n);
        while (n != 0)
        {
            n--;
            cur1 = cur1->next;
        }
        while (cur1 != cur2)
        {
            cur1 = cur1->next;
            cur2 = cur2->next;
        }
        return cur1;
    } else {
        cur1 = loop1->next;
        while (cur1 != loop1) {
            if (cur1 == loop2) {
                return loop1;
            }
            cur1 = cur1->next;
        }
        return NULL;
    }
}

ListNode* getIntersectNOde (ListNode *head1,ListNode *head2) {//开始分情况讨论
    if (head1 == NULL || head2 == NULL) {
        return NULL;
    }
    ListNode *loop1 = getLoopNode(head1);
    ListNode *loop2 = getLoopNode(head2);
    if(loop1 == NULL && loop2 == NULL) {
        return noLoop(head1, head2);
    }
    if(loop1 != NULL && loop2 != NULL) {
        return bothLoop(head1, loop1, head2, loop2);
    }
    return NULL;
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
