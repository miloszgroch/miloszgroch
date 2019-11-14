#include <stdio.h>

int main (void)
/*{
	int a, b;
	printf("Podaj liczbę\n");
	scanf("%i", &a);
	if (a<0){
		b = a*a;
		printf("Kwadrat liczby to %i\n", b);
	}
	else (a>0){
		c = (!a);
	}

}
*/

{
	int b200 = 0, b100 = 0, b50 = 0, b20 = 0, b10= 0, b5 = 0, b2 = 0, b1= 0, b05 = 0, b02 = 0, b01 = 0;
	float a, b;
	printf("Podaj liczbę\n");
	scanf("%f", &a);
	while (b>=0)
	{
		if (b>=200)
		{
			b = a - 200;
			b200+=1;
		}
		else if (b>=100)
		{
			b = b - 100;
			b100+=1;
		}
		else if (b>= 50)
		{
			b = b - 50;
			b50+=1;
		}
		else if (b>= 20)
		{
			b = b - 20;
			b20+=1;
		}
		else if (b >= 10)
		{
			b = b - 10;
			b10+=1;

		}
		else if (b>=5)
		{
			b = b - 5;
			b5+=1;
		}
		else if (b >=2)
		{
			b = b - 2;
			b2+=1;
		}
		else if (b>=1)
		{
			b = b - 1;
			b1+=1;
		}
		else if (b>=0.5)
		{
			b = b - 0.5;
			b05+=1;
		}
		else if (b>=0.2)
		{
			b = b - 0.2;
			b02+=1;
		}
		else if (b>=0.1)
		{
			b = b - 0.5;
			b01+=1;
		}
		else
		{
			break;
		}
	}
printf("%i\n%i\n%i\n%i\n%i\n%i\n%i\n%i\n%i\n%i\n%i\n", b200, b100, b50, b20, b10, b5, b2, b1, b05, b02, b01);

}




