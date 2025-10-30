// Linked list with creation, display, insertion, deletion, and search
#include <iostream>
using namespace std;

class linkedlist {
    int n;
    struct node {
        int data;
        node* link;
    } *start;

public:
    linkedlist();
    void create();
    void dis();
    void inser();
    void del();
    void search();
};

linkedlist::linkedlist() {
    start = NULL;
    n = 0;
}

void linkedlist::create() {
    cout << "How many nodes you want to create bhau? ";
    cin >> n;
    node *temp, *p = NULL;
    for (int i = 0; i < n; i++) {
        temp = new node;
        cout << "Enter data for node " << i + 1 << ": ";
        cin >> temp->data;
        temp->link = NULL;

        if (start == NULL)
            start = p = temp;
        else {
            p->link = temp;
            p = temp;
        }
    }
}

void linkedlist::dis() {
    node* temp = start;
    if (start == NULL)
        cout << "Empty linked list bhava!" << endl;
    else {
        cout << "Linked list elements: ";
        while (temp != NULL) {
            cout << temp->data << " ";
            temp = temp->link;
        }
        cout << endl;
    }
}

void linkedlist::inser() {
    int pos;
    cout << "Enter the position where you wish to insert the new node: ";
    cin >> pos;

    if (pos >= 1 && pos <= n + 1) {
        node *temp, *p;
        temp = new node;
        cout << "Enter data: ";
        cin >> temp->data;
        temp->link = NULL;

        if (pos == 1) {
            temp->link = start;
            start = temp;
        } else {
            p = start;
            for (int i = 1; i < pos - 1; i++)
                p = p->link;
            temp->link = p->link;
            p->link = temp;
        }
        n++;
        cout << "Node inserted successfully!\n";
    } else
        cout << "Invalid position dila bhava!\n";
}

void linkedlist::del() {
    int pos;
    cout << "Enter the position where you wish to delete the node: ";
    cin >> pos;

    if (pos >= 1 && pos <= n) {
        node *temp = start, *p;
        if (pos == 1) {
            start = start->link;
            delete temp;
        } else {
            for (int i = 1; i < pos - 1; i++)
                temp = temp->link;
            p = temp->link;
            temp->link = p->link;
            delete p;
        }
        n--;
        cout << "Node deleted successfully!\n";
    } else
        cout << "Invalid position dila bhava!\n";
}

void linkedlist::search() {
    int val, pos = 1;
    cout << "Enter the value to search: ";
    cin >> val;
    node* temp = start;
    while (temp != NULL) {
        if (temp->data == val) {
            cout << "Element " << val << " found at position " << pos << "!\n";
            return;
        }
        temp = temp->link;
        pos++;
    }
    cout << "Element not found bhava!\n";
}

int main() {
    linkedlist o;
    int choice;
    while (true) {
        cout << "\n--- MENU ---\n";
        cout << "1. Create linked list\n";
        cout << "2. Display linked list\n";
        cout << "3. Insert node\n";
        cout << "4. Delete node\n";
        cout << "5. Search element\n";
        cout << "6. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                o.create();
                break;
            case 2:
                o.dis();
                break;
            case 3:
                o.inser();
                break;
            case 4:
                o.del();
                break;
            case 5:
                o.search();
                break;
            case 6:
                cout << "Exiting... Bye bhava!\n";
                return 0;
            default:
                cout << "Invalid choice re bhau!\n";
        }
    }
}