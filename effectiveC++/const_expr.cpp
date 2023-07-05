#include<iostream>

template<typename T,std::size_t N>
std::size_t arrsize(T (&)[N])
{
    return N;
}

int main()
{
    int a[9];
    std::cout << arrsize(a) << std::endl;
}