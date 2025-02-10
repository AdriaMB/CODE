#include <stdio.h>


int main(void){
    int T;
    scanf("%d", &T);
    printf("%d\n", T);
    int i;
    for(i=0; i<T; i++){
        int c;
        int SS, MM, HH;
        scanf("%d", &c);
        printf("The capacity is :%d\n", c);

        SS  = c % 60;               //SS
        int aux = c/60;
        MM = aux % 60;              //MM
        HH = aux / 60;              //HH

        printf("%02d:%02d:%02d\n", HH, MM, SS);

        /*
         %02d: This format specifies that the value should be printed as an integer with at least two digits, padded with a leading zero if necessary. The 0 in the format specifier ensures padding with a zero.

         */

    }

}
