#include <stdio.h>
#include <string.h>
int main(void){
    char str[100][100];
    int marksArr[100];
    char *words;
    int n, marks = 0;
    char s[1000];
    printf("Input number of keywords : ");
    scanf("%d", &n);
    for(int i = 0; i<n; i++){
        printf("Input keyword %d : ", 1+i);
        scanf("%s", str[i]);
    }
    for(int i = 0; i<n; i++){
        printf("Input marks for keyword %d : ", 1+i);
        scanf("%d", &marksArr[i]);
    }
    fflush(stdin);
    printf("Input string : ");
    scanf("%[^\n]s", s);
    words = strtok (s," ,!\"'?.-");
    while(words != NULL){
        char * word= words;
        words = strtok (NULL," ,!\"'?.-");
        for(int i = 0; i<n; i++)
            if(strcmp(word, str[i])==0){
                marks += marksArr[i];
                strcpy(str[i],"");
                break;
            }
    }
    printf("%d", marks);
    return(0);
}

