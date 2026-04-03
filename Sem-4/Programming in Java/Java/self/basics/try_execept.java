import java.util.Scanner;
public class try_execept {

    public static void main(String[] args) {
        Scanner get__input = new Scanner(System.in);

    System.out.println("Enter numerator : ");
    float numerator= get__input.nextInt();

    System.out.println("Enter denominator : ");
    float denominator= get__input.nextInt();

    try {
        System.out.println("Result  = "+ divide(numerator,denominator));
    } 
    catch (Exception e) {

        //exception could be of any name.
        System.out.println("Zero-division error. : : "+e);
    }
    finally{
        System.out.println("-- End of program --");
    }




    }

    private static String divide(float numerator, float denominator) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'divide'");
    }
    
}
