class function_def {
    static int n1;
    static int n2;

//function-definition --->
    static void add(int n1,int n2){
        System.out.println("Function has been called.");
        System.out.println(" Sum = "+ (n1+n2) );
    }

    public static void main(String args[]){
        n1=4;
        n2=5;

    add(n1,n2);    
    }
}



