import java.util.Scanner;



public class Q4 {
    static boolean isPrime(int number){


        if (number<2){
            System.out.println("The number you entered is not a prime number");
            return false;

        }

        int i =2;

        while (i < number){
            if (number% i == 0){
                return false;
            }
            i++;
        }
        return true;
    }


    public static void main (String[] args){
        Scanner scan= new Scanner(System.in);

        System.out.println("Enter a any number : ");
        int num= scan.nextInt();

        boolean check= isPrime(num);

        if(check == true){
            System.out.println("The number you entered is a prime number.");
        }else{
            System.out.println("The number you entered is not a prime number.");


        }

    }
}
