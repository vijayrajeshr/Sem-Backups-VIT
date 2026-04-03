package tf141;

import java.util.Scanner;
public class RecursiveMath {

public static long factorial(int n) {
if (n == 0 || n == 1) {
return 1;
}
return n * factorial(n - 1);
}
public static int fibonacci(int n) {
    if (n <= 0) {
    return 0;
    } else if (n == 1) {
    return 1;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
    }
    public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    
    System.out.print("Enter a number to calculate its factorial: ");
    int factInput = scanner.nextInt();
    long factResult = factorial(factInput);
    System.out.println("Factorial of " + factInput + " is: " + factResult);
    System.out.print("Enter the number of Fibonacci terms to generate: ");
    int fibInput = scanner.nextInt();
    System.out.println("Fibonacci series up to " + fibInput + " terms:");
    for (int i = 0; i < fibInput; i++) {
    System.out.print(fibonacci(i) + " ");
    }
    System.out.println();
    scanner.close();
    }
    }
    