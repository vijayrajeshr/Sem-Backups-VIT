package Assigment;
import java.util.Scanner;

class grade_calc {
    public static void main(String[] args) {

    Scanner get__marks = new Scanner(System.in);

        System.out.println("Enter marks : ");        
        double marks = get__marks.nextInt();      
        //condition check
        if (marks>95 && marks<100){
            System.out.println("S - Grade");
        }
        else if (marks>90 && marks<95){
            System.out.println("A - Grade");
        }
        else if (marks>80 && marks<90){
            System.out.println("B - Grade");
        }
        else if (marks>70 && marks<80){
            System.out.println("C - Grade");
        }
        else if (marks>60 && marks<70){
            System.out.println("D - Grade");
        }
        else {
            System.out.println("F - Grade");
        }     
    }  
}
