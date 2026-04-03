/*maximum sum of hour glass.
i= rows;

j= columns;
*/
import java.util.*
public class Main{
    public static void Main(string[] args){
        int rows;
        int column;
        int sum;
        
        for (i = 0; i < rows - 3, i++){

            for(j=0; j < column - 3; j++){
                sum = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1] + a[i+2][j] + a[i+2][j+1] + a[i+2][j+2];
                system.out.println('Sum : '+sum)
            }
        }
    }
}

/* import java.util.Scanner; 

public class Main {

    // Correct main method signature
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of rows (minimum 3): ");
        int rows = scanner.nextInt();

        System.out.print("Enter the number of columns (minimum 3): ");
        int cols = scanner.nextInt(); // Corrected variable name to 'cols'

        if (rows < 3 || cols < 3) {
            System.out.println("Error: Matrix must be at least 3x3 to form an hour-glass.");
            scanner.close();
            return; 
        int[][] arr = new int[rows][cols];

        System.out.println("Enter the elements of the matrix:");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                System.out.print("Enter element at [" + i + "][" + j + "]: ");
                arr[i][j] = scanner.nextInt();
            }
        }

        scanner.close(); 
        int maxSum = Integer.MIN_VALUE;

        for (int i = 0; i <= rows - 3; i++) { // Loop for rows
            for (int j = 0; j <= cols - 3; j++) { 

                int currentSum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + // Top row
                                 arr[i+1][j+1] +                         // Middle element
                                 arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]; // Bottom row


                System.out.println("Hour-glass starting at (" + i + "," + j + ") sum: " + currentSum);


                if (currentSum > maxSum) {
                    maxSum = currentSum;
                }
            }
        }

        System.out.println("\nMaximum Hour-Glass Sum: " + maxSum);
    }
} */