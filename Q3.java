public class Q3 {
    public static void main(String[] args){
        double n=2000;//n is the number of current population
        double rate=0.15 ;// increasing rate every 6 months
        int periods=0;


        while(n <= 2000000){
            double increase = n* 0.15;
            n= (double) (n + increase);
            periods ++;

        }

        int years = periods/2;
        System.out.println("It takes " + years + " years for the population size to exceed 2,000,000");




        }




    }


