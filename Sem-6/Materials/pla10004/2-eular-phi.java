
/* recursive approach*/
import java.util.*
public class Main{
    public static void Main(string[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        int count = 1;
        for (int i=2;i<n;i++){
            if(gcd(i,n)==1){
                count++;
            }
        }  
        System.out.print("No of co-primes "+ count);

    }
    public static int gcd(int a,int b){
        if(a==0)
            return b;
        return gcd(b%a,a);
    }
}