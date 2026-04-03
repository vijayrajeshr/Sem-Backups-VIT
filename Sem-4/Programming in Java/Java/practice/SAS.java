package tf141;
public class SAS {
    String Name;
    int Age;

    SAS(String Name,int Age){
        this.Name=Name;
        this.Age = Age; 
    };

public static void main(String[] args) {
    SAS obj__1 = new SAS("Alex Mason",33);
    System.out.println(obj__1.Name+obj__1.Age);
}

    
}
+