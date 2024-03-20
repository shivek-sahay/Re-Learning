#include <bits/stdc++.h>
using namespace std;

int main()
{
    queue<int> q;
    queue<string> q2;

    q.push(1);
    q.push(2);
    q.push(5);
    q.push(7);

    cout << q.front() << " " << q.back() << endl;

    q.pop();
    q.pop();

    cout << q.front() << " " << q.back() << endl;

    return 0;
}