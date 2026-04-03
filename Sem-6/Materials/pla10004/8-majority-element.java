
class Main {
    public static void main(String[] args) {
        
        //majority element in array
        arr = { 2,2,2,5,2,6 }
        Scanner sc = new Scanner(System.in)
        string inp_num = sc.next()
        
        for (int i=0;i<n;i++){
            for (int j=i;j<n;j++){
                if (arr[i]==arr[j]){
                    count++;
                }
            if(count>n/2){
                return arr[i]
            }
            }
        }
        //
        System.out.println("Try programiz.pro");
    }
}