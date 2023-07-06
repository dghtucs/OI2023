#include<iostream>
using ll = long long;
template<typename T,std::size_t N>
std::size_t arrsize(T (&)[N])
{
    return N;
}
template<typename Container, typename Index> // C++14;
auto authAndAccess(Container& c, Index i) // not quite
{ // correct
 authenticateUser();
 return c[i]; // return type deduced from c[i]
}
int main()
{
    ll b;
    int a[9];
    std::cout << arrsize(a) << std::endl;
}