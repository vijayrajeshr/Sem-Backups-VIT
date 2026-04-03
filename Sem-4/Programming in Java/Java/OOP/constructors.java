class constructors {
    String Name;
    int age;
    //constructors
    
    constructors(String Name,int age){
        this.Name= Name;
        this.age=age;

        //"""this"""-- identifies current object.
    }


    public static void main(String agrs[]){
        constructors object_1 = new constructors("V", 30);
        
        
        System.out.println("Name : "+object_1.Name);
        System.out.println("age  : "+object_1.age);
    }

}
