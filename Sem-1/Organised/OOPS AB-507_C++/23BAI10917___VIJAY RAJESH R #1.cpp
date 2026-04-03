#include <iostream>
using namespace std;

int main() {
    int x;
    cout << "\n\tEnter the number you want to check for primality: " << endl;
    cin >> x;

    if (x <= 1) {
        cout << "\n\tThe given number " << x << " is not prime." << endl;
            }
            
    else if (x == 2) {
        cout << "\n\tThe given number " << x << " is prime." << endl;
            }
            
    else if (x % 2 == 0) {
        cout << "\n\tThe given number " << x << " is not prime." 
        <<endl;
            } 
    else {
        bool prime = true;
        for (int i = 3; (i * i) <= x; i += 2) {
            
            if (x % i == 0) {
                prime = false;
                break;
            }
            
        }

        if (prime) {
            cout << "\n\tThe given number " << x << " is prime."
            <<endl;
        }
        
        else {
            cout << "\n\tThe given number " << x << " is not prime."<<endl;
        }
    }

    return 0;
}
