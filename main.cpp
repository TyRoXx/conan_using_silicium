#include <boost/version.hpp>
#include <boost/thread.hpp>
#include <iostream>
#include <silicium/version.hpp>

int main()
{
	std::cout << BOOST_VERSION << '\n';
	std::cout << SILICIUM_VERSION << '\n';
	std::cout << boost::thread::hardware_concurrency() << '\n';
}
