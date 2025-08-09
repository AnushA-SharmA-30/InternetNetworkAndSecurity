#include <stdio.h> 
#include <stdlib.h> 
int main() 
{ 
    char plainText[100],cipherText[100],receivedText[100]; 
    int key; 
    printf("Enter plainText:\n"); 
    scanf("%s",plainText); 
    printf("Enter no of positions to be shifted:\n"); 
    scanf("%d",&key); 
    for(int i=0;plainText[i]!='\0';i++){ 
        cipherText[i] = plainText[i] + key % 26; 
    } 
    printf("Cipher text: %s \n",cipherText); 
    for(int i=0;cipherText[i]!='\0';i++){ 
        receivedText[i] = cipherText[i] - key % 26; 
    } 
    printf("Received text: %s \n",receivedText); 
    return 0; 
} 