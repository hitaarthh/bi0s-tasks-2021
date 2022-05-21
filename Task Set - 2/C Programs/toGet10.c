#include <stdio.h>
int main(void){
    float marks[100], sum=0.0;
    int n;
    printf("Input number of inputs : ");
    scanf("%d", &n);
    for(int i =0 ;i<n ;i++){
        input : 
        printf("Input marks in assesment %d : ", 1+i);
        scanf("%f", &marks[i]);
        if(marks[i]<0 || marks[i]>10){
            printf("Invalid marks");
            goto input;
        }
        sum += marks[i];
    }
    if(sum/n >= 9.5)
        printf("%d", 0);
    else{
        int assignments = 0;
        while(sum/n < 9.5){
            sum+=10;
            assignments ++;
            n++;
        }
        printf("%d", assignments);
    }
    return 0;
}