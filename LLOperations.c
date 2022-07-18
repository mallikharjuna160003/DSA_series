#include<stdio.h>
#include<stdlib.h>
typedef struct Node{
    int data;
    struct Node *next;
}Node;
Node *head=NULL;
void insert(int data){
    Node *newNode =(Node*)malloc(sizeof(Node));
    newNode->data=data;
    //inserting in the beginning
    newNode->next=head;
    head=newNode;
   
}
void insertEnd(int data){
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    Node *temp =head;
    while(temp->next!=NULL){
        temp = temp->next;
    }
    temp->next = newNode;
}
void deleteMiddleEle(){
    Node *fast = head,*slow = head,*p=NULL;
    while(fast!=NULL && fast->next!=NULL){
        p=slow;
        fast = fast->next->next;
        slow = slow->next;
    }
    p->next=slow->next;
    free(slow);
    
}
void printMiddleEle(){
    Node *fast = head,*slow = head;
    while(fast!=NULL && fast->next!=NULL){
        fast = fast->next->next;
        slow = slow->next;
    }
    printf("Middle data = %d",slow->data);
    
}
void detectLoop(){
    Node *fast = head,*slow = head;
    while(fast!=NULL && fast->next!=NULL){
        fast = fast->next->next;
        slow = slow->next;
    }
    if(slow == fast){
        printf("\nDetected Loop");
    }
    else{
        printf("\n No loop");
    }
}
void removeLoop(){
    Node *fast = head,*slow = head;
    while(fast!=NULL && fast->next!=NULL){
        fast = fast->next->next;
        slow = slow->next;
    }
    if(slow == head){
       while(fast->next!=slow){
           fast = fast->next;
       }
       fast->next = NULL;
    }
    else if(slow == fast){
        slow = head;
        while(slow->next !=fast->next){
            fast =fast->next;
            slow = slow->next;
        }
        fast->next = NULL;
    }
}
void reverseLL(){
    
    Node *current = head,*prev=NULL,*next=NULL;
    while(current){
        next = current->next;
        current->next = prev; // here actual reverse happens
        prev = current;
        current = next;// to move to next node in the ll
       
    }
    head = prev;
    
    
}
Node* reverse(Node* head)
{
    if (head == NULL || head->next == NULL)
        return head;

    /* reverse the rest list and put
      the first element at the end */
    Node* rest = reverse(head->next);
    head->next->next = head;

    /* tricky step -- see the diagram */
    head->next = NULL;

    /* fix the head pointer */
    return rest;
}
void deleteEndNode(){
    Node *temp = head;
    while(temp->next->next!=NULL){
        temp=temp->next;
    }
    free(temp->next);
    temp->next=NULL;
}
void deleteFrontNode(){
    Node *temp = head;
    head = head->next;
    free(temp);
}
Node* removeDup(Node *head){
    Node *temp =head;
    while(temp!=NULL && temp->next !=NULL)
    {
        if(temp->data == temp->next->data)
        {
            Node *temp1 =  temp->next;
            temp->next = temp1->next;   
            free(temp1);
        }
        else
        {
            temp=temp->next;
        }
       
    }
    return head;
}
Node* solve(Node *head,int k)
{
    Node *prev=NULL,*cur=head,*next=NULL;
    int i=0;
    while(cur && i<k)
    {
     
        i++;
        next=cur->next;
        cur->next=prev;
        prev=cur;
        cur=next;
    }
   
    if(cur!=NULL)
    {
      //cout<<prev->data<<" "<<cur->data<<endl;
      head->next=solve(cur,k);
    
    }
    else
    {
        head->next=NULL;
    }
    return prev;
}
    
Node* Preverse (Node* head, int k)
{ 
    // Complete this method
    return solve(head,k);
    
}
void display(){
    Node *temp=head;
    while(temp!=NULL){
        printf("%d->",temp->data);
        temp = temp->next;
    }
    
}
int main()
{
    int i=0;
    for(i=0;i<5;i++){
        insert(i);
    }
    for(i=10;i<=50;i+=10){
        insertEnd(i);
    }
    
    
    display();
    deleteEndNode();
    printf("\n");
    printMiddleEle();
    printf("\n");
    display();
    detectLoop();
    printf("\n");
    printMiddleEle();
    deleteFrontNode();
    printf("\n");
    display();
    printf("\n");
    printMiddleEle();
    deleteMiddleEle();
    printf("\n");
    printMiddleEle();
    reverseLL();
    printf("\n");
    display();
    printf("\n");
    head = reverse(head);
    insertEnd(1);
    insertEnd(1);
    display();
    head = removeDup(head); // its for consecutive elements
    printf("\n");
    display();
    head = Preverse(head,4);
    printf("\n");
    display();
    return 0;
}
