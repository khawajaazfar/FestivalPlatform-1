#include <iostream>
using namespace std;

class aray
{
    int a[10];
    int loc, ele, n, pos;
public:
    void display();
    void insertt();
    aray();
};

aray::aray()
{
    cout << "Enter the number of elements: ";
    cin >> n;
    cout << "Enter the elements: ";
    for (int i = 0; i < n; i++)
        cin >> a[i];
}

void aray::insertt()
{
    cout << "Enter the location (1 to " << n + 1 << ") where you wish to insert the new element: ";
    cin >> loc;
    if (loc >= 1 && loc <= n + 1)
    {
        cout << "Enter the element: ";
        cin >> ele;
        pos = n;
        while (pos >= loc)
        {
            a[pos] = a[pos - 1];
            pos--;
        }
        a[loc - 1] = ele;
        n++;
    }
    else
        cout << "Invalid entry!";
}

void aray::display()
{
    cout << "The new array after insertion is: ";
    for (int i = 0; i < n; i++)
        cout << a[i] << " ";
    cout << endl;
}

int main()
{
    aray l;
    l.insertt();
    l.display();
    return 0;
}