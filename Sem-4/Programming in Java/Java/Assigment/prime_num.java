import java.util.Scanner;

package Assigment;
public class prime_num {
    public static void main(String[] args) {
        
        Scanner get___num = new Scanner(System.in);

        int x = get___num.nextInt();

        if (x<=1){
            System.out.println("Not prime");
        }       
        else {
         for (int i = 0; 2 < x;) {
            if(x%2==0){
                System.out.println("Not prime"); 
                break;
            }
            else{
                System.out.println(x+" is a prime number.");
            }
        }
        
        }
    }
