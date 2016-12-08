#include <iostream>
#include <stack>
#include <math.h>

class Node {
    Node *right;
    Node *down;

public:
    Node(){
        right = NULL;
        down = NULL;
    }

    bool CanAdd() {
        if(!right || !down) {
            return false;
        }

        if(right->down || down->right) {
            return false;
        }

        return true;
    }

    int Visit() {
        if(!right && !down) {
            return 0;
        }

        if(!right) {
            return down->Visit();
        }

        if(!down) {
            return right->Visit();
        }

        return right->Visit() + down->Visit();
    };

    void AddRight() {
        right = new Node();
    }

    void AddDown() {
        down = new Node();
    }

    void SetRight(Node* n) {
        right = n;
    }

    void SetDown(Node* n) {
        down = n;
    }

    Node* GetRight() {
        return right;
    }

    Node* GetDown() {
        return down;
    }
};

int main()
{
    std::cout
        << " start "
        << std::endl;

    Node root;
    Node *myNode;
    myNode = &root;
    int size = 2;

    for( int i = 0; i < size; i++ ) {
        myNode->AddRight();
        Node* tempNode = myNode->GetRight();
        myNode = tempNode;
    }

    for( int i = 0; i < size; i++ ) {
        myNode->AddDown();
        Node* tempNode = myNode->GetDown();
        myNode = tempNode;
    }

    int i=0;
    Node *counter;
    // Node *temp;
    counter = &root;

    while(NULL != counter->GetRight()) {
        i++;
        std::cout
            << i
            << ": "
            << counter;

        counter = counter->GetRight();

        // std::cout
        //     << " -> "
        //     << counter;

        std::cout << std::endl;
    }

    // for( int i = 0; i < size; i++ ) {
    //     Node* newNode;
    //     root.addDown(newNode);
    // }

    // for( int i = 0; i < size; i++ ) {
    //     Node newNode;
    //     root.addRight(newNode);

    //     for( int j = 0; j < size; j++ ) {
    //         // if( i == size && j == 0) {
    //         //     Node right;
    //         //     myNode.addRight();
    //         // }
    //         // if( i == size ) {
    //         //     Node down;
    //         //     myNode.addDown(down);
    //         // // } else {
    //         // //     Node adder;

    //         // //     root.add(&adder);
    //         // }
    //     }
    // }

}
