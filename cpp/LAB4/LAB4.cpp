#include <iostream>
using namespace std;
int main(){
    class Node{
    public:
        int data;
        Node* next;
        Node(int x, Node* n){
            data = x;
            next = n;
        }
};
    class Queue{
    private:
        Node* head;
    public:
        Queue(){
            head = nullptr;
        }
        bool isEmpty(){
            return head == nullptr;
        }
        void enqueue(int x){
            if (this->isEmpty()){
                Node *a = new Node(x, nullptr);
                this->head = a;
            }
            else{
                Node *b = new Node(x,this->head);
                this->head = b;
            }
        }
        void print(){
            Node *p = nullptr;
            p=head;
            for(p=head; p!=nullptr;p=p->next){
                cout << p->data << " ";
            }
        }
        void dequeue(){
            if (!this->isEmpty()){
                Node *d = nullptr;
                for(d=head; d->next->next!= nullptr; d=d->next); //It's an iterator, clever use.
                    delete d->next;
                    d->next = nullptr;
            }

        }
        int top(){
            if (!this->isEmpty()){
                Node *t = nullptr;
                for(t=head; t->next!= nullptr; t=t->next);
                return t->data;
            }
        }
        int size(){
            if (!this->isEmpty()){
                Node *i = nullptr;
                int queueSize = 1; //Counts for the head, we're sure there is a head due to the isEmpty check
                for(i=head; i->next!= nullptr; i=i->next){
                    queueSize++;
                }
                return queueSize;
            }
        }
        void reverse(){
            if (!this->isEmpty()) {
                Node *prev = nullptr;
                Node *target = head;
                Node *next = nullptr;
                while(target != nullptr){
                    next = target->next;
                    target->next = prev;
                    prev = target;
                    target = next;
                }
                head = prev;
            }
        }
    };
    Queue *testQueue = new Queue;
    cout << "isEmpty: " << testQueue->isEmpty() << endl;
    cout << "Adding 1-2-3..." << endl;
    testQueue->enqueue(1);
    testQueue->enqueue(2);
    testQueue->enqueue(3);
    cout << "isEmpty: " << testQueue->isEmpty() << endl;
    cout << "Contents: ";
    testQueue->print();
    cout<< endl << "Top: " << testQueue->top();
    cout << endl << "Size: " <<testQueue->size() <<endl;
    cout <<"Enqueuing 4-5-6-7-8..." << endl;
    testQueue->enqueue(4);
    testQueue->enqueue(5);
    testQueue->enqueue(6);
    testQueue->enqueue(7);
    testQueue->enqueue(8);
    cout << "Contents: ";
    testQueue->print();
    cout << endl << "Reversing..." << endl;
    testQueue->reverse();
    cout << "Contents: ";
    testQueue->print();
    cout << endl << "Size: "<< testQueue->size() << endl;
}