#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double a, b, c;

    cout << "Enter the coefficient a : "<<endl;
     cin >> a;
    cout << "Enter the coefficient b : "<<endl;
     cin >> b;
    cout << "Enter the coefficient c : "<<endl;
     cin >> c;

    double fac = b * b - 4 * a * c;

    if (fac >= 0) {
        double root1 = (-b + sqrt(fac)) / (2 * a);
        double root2 = (-b - sqrt(fac)) / (2 * a);

        cout << "Root 1: " << root1 << endl;
        cout << "Root 2: " << root2 << endl;
    } else {
        cout << "All Roots are complex." << endl;
    }

    return 0;
}




