public class Try {
    public static void main(String[] args) {
        int result;
        int val = 0;
        try {
            result = val / 1;
            result = 7;
        } catch(ArithmeticException e) {
            System.out.println(e);
            result = 0;
        }
        System.out.println(result);
    }
}
