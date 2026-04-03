for(i=0;i<n;i++){
    
    current_max = arr[i]

    for(j=i+1; j<n; j++){
        ;
        temp = temp*current_max[j];
        max=math.max(temp,current_max)
    }
}
//functional code:
class GfG {

    static int max(int a, int b, int c) {
        return Math.max(a, Math.max(b, c));
    }

    static int min(int a, int b, int c) {
        return Math.min(a, Math.min(b, c));
    }
    static int maxProduct(int[] arr) {
        int n = arr.length;
        int currMax = arr[0];

        int currMin = arr[0];

        int maxProd = arr[0];

        for (int i = 1; i < n; i++) {
            

            int temp = max(arr[i], arr[i] * currMax, arr[i] * currMin);

            currMin = min(arr[i], arr[i] * currMax, arr[i] * currMin);
            currMax = temp;

            maxProd = Math.max(maxProd, currMax);
        }
        return maxProd;
    }

    public static void main(String[] args) {
        int[] arr = { -2, 6, -3, -10, 0, 2 };
        System.out.println(maxProduct(arr));
    }
}