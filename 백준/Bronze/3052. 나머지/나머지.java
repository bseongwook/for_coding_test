import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        Set<Integer> set = new HashSet<>();

        for (int i = 0; i < 10; i++) {
            int num = sc.nextInt();
            Integer n = num % 42;

            set.add(n);
        }
        System.out.println(set.size());
    }
}
