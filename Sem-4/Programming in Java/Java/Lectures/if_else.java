public class if_else {
    public static void main(String args[]){
        int z= 40;
        int x=35;

        if (z>40){
            System.out.println("z greater than 40");
        }
        else if (z<x){
            System.out.println("x is greater");
        }
        else if (x<z){
            System.out.println("z is greater");
        }
        else{
            System.out.println("None .");
        }
    }
    
}
//ternary ops = if true(==) then only execute
// eg., x=45;  if x%2==0 --> then (execution)
