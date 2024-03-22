public class PrimeNumbers {

    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Please provide some numbers!");
        }

        System.out.println("Prime numbers are:");

        for (String arg : args) {
            try {
                int num = Integer.parseInt(arg);
                if (isPrime(num)) {
                    System.out.println(num);
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid integer: " + arg);
            }
        }
    }

    private static boolean isPrime(int num) {
        if (num < 2) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
