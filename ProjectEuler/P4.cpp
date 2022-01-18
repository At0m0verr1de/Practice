#include <iostream>

using namespace std;
int main()
{    
    int product{0};
    int highest = 0;
    for(int i{999};i>=100;--i)
    {
       for(int j{999};j>=100;--j )
        {
            product=i*j;
            int reversed_number=0;
            int n=product;
            while(n!=0)
            {
              int rem=n%10;
              reversed_number=reversed_number*10+rem;
              n/=10; 
            }            
            if (reversed_number == product && reversed_number > highest){
                highest = reversed_number;
            }
        }
        }
    
        cout << highest<< endl;
    return 0;
}

