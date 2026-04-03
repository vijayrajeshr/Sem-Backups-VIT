package tf141;

class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void setDetails(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public static Person createPerson(String name, int age) {
        return new Person(name, age);
    }

    public void displayDetails() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}

public class ObjectInitializationDemo {
    public static void main(String[] args) {
        Person person1 = new Person("Walter White", 30);
        person1.displayDetails();

        Person person2 = new Person("", 0);
        person2.setDetails("James Cameron", 25);
        person2.displayDetails();

        Person person3 = Person.createPerson("A R XRahman", 40);
        person3.displayDetails();
    }
}
