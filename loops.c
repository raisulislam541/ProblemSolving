#include<stdio.h>
int main()
{
    int i,j,k,l,p;
    printf("enter the number of rows:");
    scanf("%d",&k);
    p=k;
    for(i=1; i<=k; i++)
    {
        for(j=1; j<=i; j++)
        {
            printf("*");
            if(j==i)
            {
                for(l=p; l>i; --l)
                {
                    printf(".");
                }
            }
        }

        printf("\n");
    }
}
//int i,j,k
