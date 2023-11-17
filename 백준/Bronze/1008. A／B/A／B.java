import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        double A = sc.nextDouble(); // 수정된 부분
        double B = sc.nextDouble();
        
        System.out.println(A/B);
        sc.close();
    }
}
