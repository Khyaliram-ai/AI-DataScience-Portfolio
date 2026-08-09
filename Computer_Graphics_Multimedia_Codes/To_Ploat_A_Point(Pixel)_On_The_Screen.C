#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<dos.h>

void plot(int,int,int,int);
void main()
{
 int gd = DETECT,gm;
 clrscr();

 detectgraph(&gd,&gm);

 initgraph(&gd,&gm,"C:\\TurboC3\\BGI");
 rectangle(50,50,100,100);
 plot(55,55,9,0);
 getch();

 closegraph();
}
void plot(int x,int y,int fill_col,int old_col)
{
 if(getpixel(x,y) == old_col)
 {
  delay(10);
  putpixel(x,y,fill_col);
  plot(x+1,y,fill_col,old_col);
  plot(x-1,y,fill_col,old_col);
  plot(x,y+1,fill_col,old_col);
  plot(x,y-1,fill_col,old_col);
 }
}