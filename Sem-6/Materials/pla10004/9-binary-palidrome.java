class Main {
    public static void main(String[] args) {
        int num = 9;

        // Convert number to binary string
        String binaryString = Integer.toBinaryString(num);
        System.out.println("Binary representation of " + num + " is: " + binaryString);

        //checking if string is palindrome/not
        int left = 0;
        int right = binaryString.length() - 1;
        boolean isPalindrome = true;

        while (left < right) {
            if (binaryString.charAt(left) != binaryString.charAt(right)) {
                isPalindrome = false;
                break;
            }
            left++;
            right--;
        }

        // Print the result
        if (isPalindrome) {
            System.out.println("The binary string is a palindrome.");
        } 
        
        else {
            System.out.println("The binary string is NOT a palindrome.");
        }
    }
}


