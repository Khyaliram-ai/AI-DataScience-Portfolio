#include<stdio.h>
#include<conio.h>
#include<graphics.h>

void drawcircle(int xc,int yc,int radius)
{
 int x = radius;
 int y = 0;
 int err = 0;

 while(x>=y) {
   putpixel(xc + x , yc + y , 7);
   putpixel(xc + y , yc + x , 7);
   putpixel(xc - y , yc + x , 7);
   putpixel(xc - x , yc + y , 7);
   putpixel(xc - x , yc - y , 7);
   putpixel(xc - y , yc - x , 7);
   putpixel(xc + y , yc - x , 7);
   putpixel(xc + x , yc - y , 7);

 if(err<=0)
  {
   y += 1;
   err += 2 * y + 1;
  }
 if(err>=0)
  {
   x -= 1;
   err = 2 * x + 1;
  }
 }
}
int main()
 {
 int gdriver = DETECT , gm , err , x , y , r;

 initgraph(&gdriver , &gm , "C:\\TurboC3\\BGI");

 printf("Enter the radius of circle:");
 scanf("%d", &r);

 printf("Enter coordinates of center(x and y):");
 scanf("%d%d" , &x , &y);

 drawcircle(x , y ,r);
 return 0;
}