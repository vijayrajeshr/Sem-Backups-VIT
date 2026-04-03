#include <iostream>
using namespace std;

const int N = 3; 

class Matrix {
private:
    int mat[N][N];

public:
    Matrix() {
        // Initialize the matrix with zeros
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                mat[i][j] = 0;
            }
        }
    }

    // Overload the + operator for matrix addition using friend function
    friend Matrix operator+(Matrix matrix1, Matrix matrix2);

    // Overload the - operator for matrix subtraction using friend function
    friend Matrix operator-(Matrix matrix1, Matrix matrix2);

    // Overload the * operator for matrix multiplication
    Matrix operator*(Matrix other) {
        Matrix result;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < N; k++) {
                    result.mat[i][j] += mat[i][k] * other.mat[k][j];
                }
            }
        }
        return result;
    }

    // Overload the * operator for scalar multiplication
    Matrix operator*(int scalar) {
        Matrix result;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                result.mat[i][j] = mat[i][j] * scalar;
            }
        }
        return result;
    }

    // diplaying matrix
    void display() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cout << mat[i][j] << " ";
            }
            cout << endl;
        }
    }
};

// Define the friend function for matrix addition
Matrix operator+(Matrix matrix1, Matrix matrix2) {
    Matrix result;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            result.mat[i][j] = matrix1.mat[i][j] + matrix2.mat[i][j];
        }
    }
    return result;
}

// Define the friend function for matrix subtraction
Matrix operator-(Matrix matrix1, Matrix matrix2) {
    Matrix result;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            result.mat[i][j] = matrix1.mat[i][j] - matrix2.mat[i][j];
        }
    }
    return result;
}

int main() {
    Matrix mat1, mat2;

    cout << "Matrix 1:" << endl;
    mat1.display();

    cout << "Matrix 2:" << endl;
    mat2.display();

    // Perform addition using the friend function
    cout << "Matrix 1 + Matrix 2:" << endl;
    (mat1 + mat2).display();

    // Perform subtraction using the friend function
    cout << "Matrix 1 - Matrix 2:" << endl;
    (mat1 - mat2).display();

    // Perform multiplication
    cout << "Matrix 1 * Matrix 2:" << endl;
    (mat1 * mat2).display();

    // Scalar multiplication
    int scalar = 3;
    cout << "Matrix 1 * " << scalar << ":" << endl;
    (mat1 * scalar).display();

    return 0;
}
