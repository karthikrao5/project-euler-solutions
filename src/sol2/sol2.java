public class sol1 {

    private int sum = 0;

    public static void main(String[] args) {
        fib(10);
        System.out.println(sum);
    }

    public void fib(n) {
        if (n == 1) {
            return 1;
        } else if (n == 0) {
            return 0;
        }

        if (n % 2 == 0 and n < 4_000_000) {
            sum += n;
        }

        return fib(n - 1) + fib(n - 2);
    }
}