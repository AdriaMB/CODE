import java.util.Scanner;

public class bitpp{
    public static void main(String[] args){
        Scanner kbd = new Scanner(System.in);

        int res = 0;
        int n = Integer.parseInt(kbd.nextLine());

        for(int i = 0; i < n; i++){
            String line = kbd.nextLine();
            char operation = line.charAt(1);
            switch(operation){
                case '+':
                    //System.out.println("++");
                    res++;
                    break;
                case '-':
                    //System.out.println("--");
                    res--;
                    break;
                default:
                    break;
            }
        }
        System.out.println(res);
    }
}
