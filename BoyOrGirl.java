import java.util.Scanner;

public class BoyOrGirl{
    public static void main(String[]args){
        Scanner in = new Scanner(System.in);
        String name = in.nextLine();
        char[] letters = new char[name.length()];
        char aux;
        int elem = 0;
        int count = 0;

       
        for(int i = 0; i < name.length(); i++){
            aux = name.charAt(i);
            if(!contains(aux, elem, letters)){
                count++;
                letters[i] = aux;
                elem++;
            }
        }
        //IT WORKS!!!!!!!!!!
        System.out.println(count%2==0 ? "CHAT WITH HER" :"IGNORE HIM");


    }

    public static boolean contains(char c, int elem, char[] theArray)
    {
        //Given a char, checks whether is contained in the first elements of theArray[]
        for(int i = 0; i < elem; i++){
            if(c == theArray[i]) return true;
        }
        return false;

    }



}
