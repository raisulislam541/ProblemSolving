#include<stdio.h>
int main()
{
    int i,j,k,p,l;

    printf("enter the number of rows:");
    scanf("%d",&k);
    p=k;

    for(i=k; i>0; i--)
    {
        for(j=1; j<=i; j++)
        {
            if(i<k)
            {
                for(l=i; l<p; ++l)
                {
                    printf(".");
                    // k--;
                }
                k--;
            }
            printf("*");

        }
        //  p=k;
        printf("\n");
    }
    return 0;

}
