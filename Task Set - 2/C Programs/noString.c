#include <stdio.h>
int main(void){
    char a[1000], b[1000];
    int i = 0;
    printf("Input string a : ");
    scanf("%[^\n]s", a);
    fflush(stdin);
    printf("Input string b : ");
    scanf("%[^\n]s", b);
    while(1){
        if(a[1+i]=='\0'&& b[1+i] =='\0'){
            printf("Equal");
            break;
        }
        else if(a[1+i]=='\0'){
            printf("First");
            break;
        }
        else if(b[1+i]=='\0'){
            printf("Second");
            break;
        }
        i++;
    }
    return 0;
}