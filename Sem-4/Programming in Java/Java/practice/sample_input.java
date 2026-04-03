package tf141;

import java.util.Scanner;

public class sample_input{

    public static void main(String []args){

    System.out.println("--Input Program--");
    Scanner input = new Scanner(System.in);

    System.out.println("enter name : ");
    String get_name = input.nextLine();

    System.out.println("enter age : ");
    int get_id = input.nextInt();

    System.out.println(" Name  : "+get_name);
    System.out.println(" ID    : "+get_id);


    }
}
