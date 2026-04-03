package Assigment;

import java.util.Random;

public class RandomNumberGenerator {
    public static void main(String[] args) {
        Random rand = new Random();

        // Generate a random integer between 0 and 100 (inclusive)
        int randomInt = rand.nextInt(101);
        System.out.println("Random integer: " + randomInt);

        // Generate a random double between 0 and 1
        double randomDouble = rand.nextDouble();
        System.out.println("Random double: " + randomDouble);
    }
}