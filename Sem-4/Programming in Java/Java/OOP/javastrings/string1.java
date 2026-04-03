package OOP.javastrings;
class StringComparisonUsingEqualsMethod{  
    public static void main(String args[]){  
      String s1="vijay";  
      String s2="rajesh r";  
      String s3=new String("rajesh r");  
      String s4="Saurav";  
      System.out.println(s1.equals(s2));//true  
      System.out.println(s1.equals(s3));//true  
      System.out.println(s1.equals(s4));//false  
    }  
   }  