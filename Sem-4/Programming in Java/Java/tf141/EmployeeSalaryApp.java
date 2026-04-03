package tf141;

import java.util.Scanner;
class Employee {
    private String name;
    private String position;
    private double baseSalary;
    private double bonus;

    public Employee(String name, String position, double baseSalary, double bonus) {
        this.name = name;
        this.position = position;
        this.baseSalary = baseSalary;
        this.bonus = bonus;
    }

    public double calculateSalary() {
        return baseSalary + bonus;
    }

    public void displayDetails() {
        System.out.println("Employee Name: " + name);
        System.out.println("Position: " + position);
        System.out.println("Base Salary: $" + baseSalary);
        System.out.println("Bonus: $" + bonus);
        System.out.println("Total Salary: $" + calculateSalary());
    }
}

public class EmployeeSalaryApp {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter employee name: ");
        String name = scanner.nextLine();
        System.out.print("Enter position: ");
        String position = scanner.nextLine();
        System.out.print("Enter base salary: ");
        double baseSalary = scanner.nextDouble();
        System.out.print("Enter bonus: ");
        double bonus = scanner.nextDouble();

        Employee employee = new Employee(name, position, baseSalary, bonus);
        employee.displayDetails();

        scanner.close();
    }
}
