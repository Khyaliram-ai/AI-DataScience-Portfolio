#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <graphics.h>

int main() {
    int gd = DETECT, gm;
    int X1, Y1, X2, Y2, steps, k;
    float Xincr, Yincr, X, Y, dx, dy;

    printf("Enter X1, Y1: ");
    if (scanf("%d %d", &X1, &Y1) != 2) return 1;
    
    printf("Enter X2, Y2: ");
    if (scanf("%d %d", &X2, &Y2) != 2) return 1;

    initgraph(&gd, &gm, "");

    dx = (float)(X2 - X1);
    dy = (float)(Y2 - Y1);

    if (abs((int)dx) > abs((int)dy)) {
        steps = abs((int)dx);
    } else {
        steps = abs((int)dy);
    }

    Xincr = dx / (float)steps;
    Yincr = dy / (float)steps;

    X = (float)X1;
    Y = (float)Y1;

    putpixel((int)(X + 0.5), (int)(Y + 0.5), WHITE);

    for (k = 1; k <= steps; k++) {
        delay(10);
        X += Xincr;
        Y += Yincr;
        putpixel((int)(X + 0.5), (int)(Y + 0.5), WHITE);
    }

    outtextxy(200, 20, "DDA Line Drawing");
    outtextxy(X1 + 5, Y1 - 5, "(X1, Y1)");
    outtextxy(X2 + 5, Y2 + 5, "(X2, Y2)");

    getch();
    closegraph();
    return 0;
}
