public class Maximum {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Please provide some numbers!");
        }

        double max = Double.parseDouble(args[0]);
        for (int i = 1; i < args.length; i++) {
            double current = Double.parseDouble(args[i]);
            if (current > max) {
                max = current;
            }
        }
        System.out.println("Maximum value is: " + max);
    }
}
