public class EquilibriumIndex {
    public static void main(String[] args) {
        int[] arr = {1, 3, 5, 2, 2}; //example 
        int n = arr.length;

        for (int i = 0; i < n; i++) {
            int leftSum = 0;
            int rightSum = 0;

            for (int j = 0; j < i; j++) {
                leftSum += arr[j];
            }

            for (int j = i + 1; j < n; j++) {
                rightSum += arr[j];
            }

            if (leftSum == rightSum) {
                System.out.println("Equilibrium index: " + i);
                return;
            }
        }

        System.out.println("No Equilibrium index found.");
    }
}
//method- 2 :
left[0] = arr[0];
for (i=1;i<n;i++){
    left[i] = left[i-1] + arr[i]
    }

//method- 3:
left = 0
for(i ==0;i<n;i++){
    right = tot - left - cur[i];
    if (right==left){
        return left+arr[i];
    }
    left = left+arr[i];
}

3