package Assigment;

public class std_mark_list {
    static String std_name;
    static int std_id;
    static int std_marks;
    
    std_mark_list(String std_name,int std_id,int std_marks){
        this.std_name=std_name;
        this.std_id=std_id;
        this.std_marks=std_marks;
    }
    static void show__student(String std_name,int std_id,int std_marks){
        System.out.println("Name  : "+std_name);
        System.out.println("ID    : "+std_id);
        System.out.println("Marks : "+std_marks);
    }
    public static void main(String[] args) {
        std_mark_list std___1 = new std_mark_list("Narendra Modi", 635001, 98);
        std___1.show__student(std_name, std_id, std_marks);

    }
}
