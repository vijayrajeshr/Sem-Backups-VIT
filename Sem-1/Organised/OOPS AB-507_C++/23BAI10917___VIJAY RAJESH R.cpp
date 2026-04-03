#include <iostream>
#include <cmath>

using namespace std;

class myint {
private:
    int n;

public:
    myint(int value) : n(value) {}

    void getInput() {
        cout << "Enter an integer: ";
        cin >> n;
    }

    long long factorial() {
        if (n < 0) {
            return -1; // indicates invalid input
        }
        long long result = 1;
        for (int i = 1; i <= n; ++i) 
        {
            result *= i;
        }
        return result;
    }

    int sum1() {
        int sum = 0;
        int temp = n;
        while (temp != 0) {
            sum += temp % 10;
            temp /= 10;
        }
        return sum;
    }

    double squareRoot() {
        if (n < 0) {
            return -1; // for invalid input
        }
        return sqrt(n);
    }

    double cubeRoot() {
        return cbrt(n);
    }

    string even() {
        return n % 2 == 0 ? "Yes" : "No";
    }

    string odd() {
        return n % 2 != 0 ? "Yes" : "No";
    }

    string perfectSquare() {
        if (n < 0) {
            return "No"; //for negative numbers are not perfect squares
        }
        int sqrtN = sqrt(n);
        return sqrtN * sqrtN == n ? "Yes" : "No";
    }

    string palindrome() {
        int original = n;
        int reversed = 0;
        while (n > 0) {
            int digit = n % 10;
            reversed = reversed * 10 + digit;
            n /= 10;
        }
        return original == reversed ? "Yes" : "No";
    }

    string divisible(int x) {
        return n % x == 0 ? "Yes" : "No";
    }
};

int main() {
    int value;
    cout << "\n\tEnter an integer value: ";
    cin >> value;

    myint num(value);

    cout << "\n\tFactorial: " << num.factorial() << endl;

    cout << "\n\tSum of Digits: " << num.sum1() << endl;

    cout << "\n\tSquare Root: " << num.squareRoot() << endl;

    cout << "\n\tCube Root: " << num.cubeRoot() << endl;

    cout << "\n\tEven: " << num.even() << endl;

    cout << "\n\tOdd: " << num.odd() << endl;

    cout << "\n\tPerfect Square: " << num.perfectSquare() << endl;

    cout << "\n\tIs Palindrome: " << num.palindrome() << endl;
    
    int x;
    cout << "\n\tEnter a divisor to check divisibility: ";
    cin >> x;
    cout << "\n\tIs Divisible by " << x << ": " << num.divisible(x) << endl;

    return 0;
}
