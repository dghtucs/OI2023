#include<iostream>
template<typename T>
auto add_(T a,T b)
{
    return a+b;
}
int main()
{
   
    std::cout << add_(1,2) << std::endl;
}