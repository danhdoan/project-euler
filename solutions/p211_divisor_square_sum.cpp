#include <iostream>
#include <chrono>
#include <vector>
#include <cmath>
using namespace std;

int process(int N) {
	vector<long> sigma(N, 1);
	for (int i = 2; i <= N/2; i++) {
		for (int j = 2*i; j < N; j += i) {
			sigma[j] += (long)i*i;
		}
	}

	int ans = 0;
	for (int i = 2; i < N; i++) {
		sigma[i] += (long)i*i;
		long x = sqrt(sigma[i]);
		if (x*x == sigma[i]) 
			ans += i;
	}

	return ans + 1;
}


int main() {
	int N = 64000000;

	auto start_t = chrono::high_resolution_clock::now();
	int ans = process(N);
	auto stop_t = chrono::high_resolution_clock::now();
	auto prx_t = chrono::duration_cast<chrono::milliseconds>(stop_t - start_t);
	cout << "Answer: " << ans 
		<< " Processing time: " << prx_t.count() << "ms" << endl;

	return 0;
}
