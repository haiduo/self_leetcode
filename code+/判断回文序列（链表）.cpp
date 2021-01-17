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

bool isPalindrom(ListNode *head){
    if(head == NULL || head->next == NULL){
        return true;
    }
    ListNode *n1 = head;
    ListNode *n2 = head;
    while(n2->next != NULL && n2->next->next != NULL){//find mind node
        n1 = n1->next;
        n2 = n2->next->next;
    }
    n2 = n1->next;
    n1->next = NULL;
    ListNode *n3 = NULL;
    while (n2 != NULL){//right part convert
        n3 = n2->next;
        n2->next =n1;
        n1 = n2;
        n2 =n3;
    }
    n3 =n1;
    n2 =head;
    bool res =true;
    while (n1 != NULL && n2 != NULL){//check palindrome
        if (n1->value != n2->value){
            res = false;
            break;
        }
        n1 = n1->next;
        n2 = n2->next;
    }
    n1 = n3->next;
    n3->next = NULL;
    while (n1 != NULL){//recover list
        n2 = n1->next;
        n1->next = n3;
        n3 = n1;
        n1 = n2;
    }
    return res;
} 
int main(){
    ListNode *head = NULL;
    for (int i = 0; i < 4; i++)
        CreateList(head, i);
    for (int i = 5; i > -1; i--)
        CreateList(head, i);
    printList(head);
    cout<<isPalindrom(head)<<endl;
    system("pause");
    return 0;
}