#include<bits/stdc++.h>
using namespace std;

int main()
{

    int arra[100];
    int i,j,k,l;
    cin>>k;
    for(i=0;i<k;i++)
    {
        cin>>arra[i];

    }
    int max1=arra[0];
    int max2;
   // j=sizeof(arra)/sizeof(arra[0]);
    for(i=1;i<k;i++)
    {
        if(arra[i]>max1)
        {
            max2=max1;
            max1=arra[i];
        }
        else if(arra[i]<max1 && arra[i]>max2)
        {
            max2=arra[i];
        }
    }
    cout<<max1<<" "<<max2;

}
