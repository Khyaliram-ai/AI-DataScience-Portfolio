%{
#include <stdio.h>
#include <stdlib.h>
%}

%%

[7-9][0-9]{9}                                   { printf("Valid Mobile Number: %s\n", yytext); }

http[s]?:\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}       { printf("Valid URL: %s\n", yytext); }

([0-2][0-9]|3[0-1])\/([0][1-9]|1[0-2])\/[0-9]{4} { printf("Valid Date: %s\n", yytext); }

([0-1]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]       { printf("Valid Time: %s\n", yytext); }

[_a-zA-Z][_a-zA-Z0-9]*                           { printf("Valid Identifier: %s\n", yytext); }

[ \t\n\r]+                                       { /* Skip whitespaces */ }

.                                                { printf("Invalid input: %s\n", yytext); }

%%

int yywrap() {
    return 1;
}

int main(int argc, char **argv) {
    if (argc > 1) {
        FILE *file = fopen(argv[1], "r");
        if (!file) {
            printf("Error opening file: %s\n", argv[1]);
            return 1;
        }
        yyin = file;
    }
    yylex();  // Start lexical analysis
    return 0;
}