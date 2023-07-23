#include<iostream>
using namespace std;

struct Node
{
    /* data */
    int data;
    Node* next;
};

int main()
{
    Node* head = new Node;
    Node* p,*q;
    int x;
    cin >> x;
    p = head;
    while (x != -1)
    {
        /* code */
        q = new Node;
        q->data = x;
        q->next = nullptr;
        p->next = q;
        p = q;
        cin >> x;
    }
    p = head->next;
    while (p->next != nullptr)
    {
        /* code */
        cout << p->data << " -> ";
        p = p->next;
    }
    cout << p->data;
    
}
























