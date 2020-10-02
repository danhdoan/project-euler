#include <iostream>
#include <chrono>
#include <cmath>
using namespace std;

long process() {
}


int main() {
	auto start_t = chrono::high_resolution_clock::now();
	long ans = process(1000);
	auto stop_t = chrono::high_resolution_clock::now();
	auto prx_t = chrono::duration_cast<chrono::milliseconds>(stop_t - start_t);
	cout << "Answer: " << ans 
		<< " Processing time: " << prx_t.count() << "ms" << endl;

	return 0;
}
