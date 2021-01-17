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

    ListNode* listPartition(ListNode *head, int pivot) {
        ListNode *sH = NULL; // small head
        ListNode *sT = NULL; // small tail
        ListNode *eH = NULL; // equal head
        ListNode *eT = NULL; // equal tail
        ListNode *mH = NULL; // big head
        ListNode *mT = NULL; // big tail
        ListNode *nex = NULL; // save next node
        //every node distribute to three lists
        while (head != NULL) {
            nex = head->next;
            head->next = NULL;
            if (head->value < pivot) {
                if(sH == NULL) {
                    sH = head;
                    sT = head;
                }else {
                    sT->next = head;
                    sT = head;
                }
            }else if (head->value == pivot) {
                if (eH == NULL){
                    eH = head;
                    eT = head;
                }else {
                    eT->next = head;
                    eT = head;
                }
            }else {
                if (mH == NULL){
                    mH = head;
                    mT = head;
                }else {
                    mT->next = head;
                    mT = head;
                }
            }
            head = nex;
        }
        //small and equal reconnect
        if (sT != NULL) {
            sT->next = eH;
            eT = eT == NULL ? sT : eT;
        }
        if (eT != NULL){
            eT->next = mH;
        }
        return sH != NULL ? sH : (eH != NULL ? eH : mH);
    }

int main(){
    ListNode *head = NULL;
    for (int i = 0; i < 10; i++)
        CreateList(head, i);
    printList(head);
    int pivot;
    cin>>pivot;
    head = listPartition(head, pivot);
    printList(head);
    system("pause");
    return 0;
}