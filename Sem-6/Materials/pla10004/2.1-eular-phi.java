import java.util.Scanner; // Import Scanner for user input

public class Main {

    // Corrected main method signature
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in); // Create a Scanner object for input
        System.out.print("Enter a positive integer n: ");
        int n = scanner.nextInt(); // Read the integer from the user

        // Calculate Euler's Totient Function
        int result = n; // Initialize result with n

        // Loop from p = 2 up to sqrt(n)
        for (int p = 2; p * p <= n; p++) {
            // If p divides n, it's a prime factor
            if (n % p == 0) {
                // Subtract result / p from result
                // This is equivalent to result = result * (1 - 1/p)
                result = result - (result / p);

                // Divide n by p repeatedly until it's no longer divisible
                // This removes all occurrences of the prime factor p
                while (n % p == 0) {
                    n = n / p;
                }
            }
        }

        // If n is still greater than 1 after the loop,
        // it means the remaining n is a prime factor itself
        if (n > 1) {
            result = result - (result / n);
        }

        System.out.println("Euler's Totient Function (phi) for " + n + " is: " + result);
    }
}