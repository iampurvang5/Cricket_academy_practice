

// public class php {
    
//     public static void main(String[] args){

//         String str = "hello";
//         String rev = "";
//         int len=str.length();

//         for(int i=0;i<=len;i++){

//             rev= str.charAt(i) + rev;

//         }
//         System.out.println(rev);
//     }
    
// }

public class php{
    public static int fibonacci(int n){
        
        if(n<=1)
            return n;
            return fibonacci(n-1)+fibonacci(n-2);
        
        
    }
    public static void main(String args[]){

        int n = 10;
        System.out.println(fibonacci(n));
    }
}