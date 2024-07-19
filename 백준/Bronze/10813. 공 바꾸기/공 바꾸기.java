import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        int[] arr = new int[N+10];

        for (int i = 1; i < N + 1; i++) {
            arr[i] = i;
        }

        for (int i = 0; i < M; i++) {
            int temp;
            int a = sc.nextInt();
            int b = sc.nextInt();

            temp = arr[a];
            arr[a] = arr[b];
            arr[b] = temp;
        }

        for (int i = 1; i < N + 1; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}