import java.util.*;

public class Main {
  public static void main(String[] args) {
      Scanner sc = new Scanner(System.in)
      int n = sc.nextInt();


      boolean[] prime = new boolean[n+1];
      for (int i = 2; i<=n;i++)
        prime[i]=true;

      for(int p = 2; p*p<=n; p++){
        if (prime[p]){
          for (int i=p*p;i<=n;i=i+p){
            prime[i]=false;
          }
        }
      }
      
      int count=0;

  }
}