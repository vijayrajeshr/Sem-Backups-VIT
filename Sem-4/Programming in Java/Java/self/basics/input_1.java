import java.util.Scanner;

class input_1 {
    public static void main(String args[]){

        @SuppressWarnings("resource")
        Scanner get__input = new Scanner(System.in);

//input statements--------------------------------------

        System.out.println(" Enter your name : ");
        String name= get__input.nextLine();
        
        System.out.println(" Enter your age : ");
        int age= get__input.nextInt();

       

//End of inputs ---------------------------------------------


        System.out.println(" Hello "+name+" . Your age is "+age);

    }
}