package tf141;

import java.util.Scanner;

class Calculator {

    // User-defined method to add two numbers
    public int add(int a, int b) {
        return a + b;
    }

    // User-defined method to calculate square of a number
    public int square(int num) {
        return num * num;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Calculator calculator = new Calculator();

        // Input for addition
        System.out.print("Enter two numbers to add: ");
        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();
        int sum = calculator.add(num1, num2);
        System.out.println("Sum: " + sum);

        // Input for square calculation
        System.out.print("Enter a number to find its square: ");
        int squareNum = scanner.nextInt();
        int squareResult = calculator.square(squareNum);
        System.out.println("Square: " + squareResult);

        // Using a predefined method (Math.sqrt) to find square root
        System.out.print("Enter a number to find its square root: ");
        double sqrtNum = scanner.nextDouble();
        double sqrtResult = Math.sqrt(sqrtNum);
        System.out.println("Square root: " + sqrtResult);

        scanner.close(); // Close the scanner to prevent resource leaks
    }
}
