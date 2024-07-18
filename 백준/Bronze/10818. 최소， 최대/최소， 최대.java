import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int maxNum = -1000000;
        int minNum = 1000000;

        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();

            if (num <= minNum) {
                minNum = num;
            }

            if (num >= maxNum) {
                maxNum = num;
            }
        }

        sc.close();

        System.out.println(minNum + " " + maxNum);
    }
}
