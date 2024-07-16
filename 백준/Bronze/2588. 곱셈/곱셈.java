import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int line1 = scanner.nextInt();
        int line2 = scanner.nextInt();
        scanner.close();

        System.out.println(line1 * (line2 % 10));
        System.out.println(line1 * ((line2 % 100) / 10));
        System.out.println(line1 * (line2 / 100));
        System.out.println(line1 * line2);
    }
}
