import java.util.Scanner;

public class Q2 {
    public static void main(String[] args){
        int even_sum=0;
        int odd_sum=0;

        int i;

        Scanner scan=new Scanner(System.in);
        System.out.println("Enter a positive integer, n:  ");
        int n= scan.nextInt();
        System.out.println("You entered the number: " + n);

        for(i=1;i<=2*n;i++){
            if(i % 2 == 0){
                even_sum= even_sum + i;

            }else{
                odd_sum=odd_sum + i;


            }

        }

        System.out.println("The sum of the first " + n + " even numbers is: " + even_sum);
        System.out.println("The sum of the first " + n + " odd numbers is: " + odd_sum);


    }

}
