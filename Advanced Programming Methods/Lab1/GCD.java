public class GCD {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Please provide some numbers!");
        }

        int gcd = Integer.parseInt(args[0]);
        for (int i = 1; i < args.length; i++) {
            int num = Integer.parseInt(args[i]);
            gcd = findGCD(gcd, num);
        }

        System.out.println("The GCD is: " + gcd);
    }

    public static int findGCD(int a, int b) {
        while (b != 0) {
            int r = a % b;
            a = b;
            b = r;
        }
        return a;
    }
}
