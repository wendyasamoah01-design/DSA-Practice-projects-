public class Q1 {
    public static void interchange(int x,int y){
        y=(x*y) /y;
        x=x+y;

        System.out.println("x = "+ x);
        System.out.println("y =" + y);

    }
    public static void main(String[] args){
        int x=10;
        int y=20;

        interchange (x, y);



}


}


