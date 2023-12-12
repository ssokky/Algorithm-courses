import java.util.Scanner;

public class MinFunction {
    static int min(int a, int b, int c, int d) {
        int min_value = a;
        
        if (b < min_value) {
            min_value = b;
        }
        
        if (c < min_value) {
            min_value = c;
        }
        
        if (d < min_value) {
            min_value = d;
        }
        
        return min_value;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();
        int d = scanner.nextInt();
        
        int result = min(a, b, c, d);
        
        System.out.println(result);
    }
}
