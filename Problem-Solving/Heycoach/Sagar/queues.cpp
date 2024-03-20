#include<bits/stdc++.h>
using namespace std;

class Queue {
    private:
        int Front, Rear;
    public:
        int capacity, queue_size, *array;

        Queue() {
            // front and Rear are indices of the array
            queue_size = 0;
            Front = 0;
            Rear = -1;
        }

        // All these function will give output or
        // perform something
        void size(int x);
        bool isEmpty();
        bool isFull();

        void enqueue(int x); // inserting into queue
        int dequeue(); // removeing from queue

        int front();
        int rear();
};

//Fuction Implementation
void Queue::size(int x) {
    capacity = x;
    array = new int[capacity]();
}

bool Queue::isEmpty() {
    return queue_size == 0 ? true : false;
}

bool Queue::isFull() {
    return queue_size == capacity ? true : false;
}

void Queue::enqueue(int x) {
    array[++Rear] = x;
    queue_size++;
}

int Queue::dequeue() {
    // first element in the queue will be removed
    int item = array[Front];

    // circular representation of the queue.
    Front = (Front + 1)%capacity;
    queue_size--;
    return item;
}

int Queue::front() {
    return array[Front];
}

int Queue::rear() {
    return array[Rear];
}


int main() {
    Queue q;

    q.size(5);

    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(5);
    q.enqueue(7);

    cout << q.front() << " " << q.rear() << endl;

    cout << q.dequeue() << endl;
    cout << q.dequeue() << endl;

    q.enqueue(9);

    cout << q.front() << " " << q.rear() << endl;
    return 0;
}