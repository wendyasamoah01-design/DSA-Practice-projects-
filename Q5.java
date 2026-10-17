
import java.util.Scanner;

public class Q5 {

    public static double calculateNetPay(int hoursWorked,String gender){

        final double INCOME_TAX=0.15;
        final double HEALTH_LEVY = 0.025;
        final double DISTRICT_TAX = 0.01;
        final double TOTAL_TAX = 0.185;


        double regularRate;
        if (gender.equalsIgnoreCase("female")) {
            regularRate = 550;

        }else {
            regularRate = 500;

        }

            double grossPay;
        if (hoursWorked<=40){
            grossPay = hoursWorked * regularRate;

        }else{
            double regularPay = 40 * regularRate;
            double overtimeHours = hoursWorked - 40;
            double overtimePay = overtimeHours * regularRate * 1.5;

            grossPay = regularPay + overtimePay;

        }

        double totalTax = grossPay * (INCOME_TAX + HEALTH_LEVY + DISTRICT_TAX);

        double netPay = grossPay - totalTax;

        return netPay;


    }

    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);

        System.out.println("How many hours did you work? ");
        int hoursWorked=scan.nextInt();

        System.out.println("Are you a male or female");
        String gender= scan.next().toLowerCase();

        double netPay = calculateNetPay(hoursWorked, gender);

        System.out.println("Your net pay as a " + gender + " employee is: " + netPay);




    }
}
