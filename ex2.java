public class ex2 {

    public int factorial(int n) {

        if (n == 0 || n == 1) {
            return 1;
        } else {
            int fact = n * factorial(n - 1);
            return fact;
        }
    }

    public static void main(String[] args) {

        ex2 obj = new ex2();

        int result = obj.factorial(5);

        System.out.println("The factorial is: " + result);
    }
}