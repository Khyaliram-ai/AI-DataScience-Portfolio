#include <stdio.h>
#include <string.h>

int isKeyword(char str[]) {
    char *keywords[] = {
        "auto", "break", "case", "char", "const", "continue", "default", 
        "do", "double", "else", "enum", "extern", "float", "for", "goto", 
        "if", "int", "long", "register", "return", "short", "signed", 
        "sizeof", "static", "struct", "switch", "typedef", "union", 
        "unsigned", "void", "volatile", "while"
    };
    int n = 32; 
    int i;
    
    for (i = 0; i < n; i++) {
        if (strcmp(str, keywords[i]) == 0)
            return 1;
    }
    return 0;
}

int main() {
    char word[50];
    printf("Enter a word: ");
    scanf("%49s", word);
    
    if (isKeyword(word))
        printf("%s is a C Keyword.\n", word);
    else
        printf("%s is Not a C Keyword.\n", word);
        
    return 0;
}

