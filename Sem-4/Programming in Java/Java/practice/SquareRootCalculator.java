package tf141;

import java.util.Scanner;  
public class SquareRootCalculator {  
public static void main(String[] args)    
{   
System.out.print("Enter a number: ");  
 
Scanner sc = new Scanner(System.in);  

int n = sc.nextInt();  

System.out.println("The square root of "+ n+ " is: "+squareRoot(n));  
}  

public static double squareRoot(int num)   
{  
//temporary variable  
double t;  
double sqrtroot=num/2;  
do   
{  
t=sqrtroot;  
sqrtroot=(t+(num/t))/2;  
}   
while((t-sqrtroot)!= 0);  
return sqrtroot;  
}  
}  