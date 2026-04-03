package Assigment;
public class emp_info_constuc {

    String emp_name;
    String emp_id;
    int emp_sal;

    //employee info using constructor
    emp_info_constuc(String emp_name,String emp_id,int emp_sal){
        this.emp_name=emp_name;
        this.emp_id=emp_id;
        this.emp_sal=emp_sal;
    }
 
public static void main(String[] args) {
    emp_info_constuc emp__1 = new emp_info_constuc("MODI", "INFO2305", 100000);
    System.out.println("Name   : "+emp__1.emp_name);
    System.out.println("ID     : "+emp__1.emp_id);
    System.out.println("Salary : "+emp__1.emp_sal);
}
}
