#include <iostream>
#include <chrono>
#include <cmath>
#include <set>
using namespace std;


bool isPal(long x) {
	long y = 0, t = x;
	while (t) {
		y = y*10 + t % 10;
		t /= 10;
	}
	return x == y;
}


long process(int N) {
	long sum = 1;
	set<long> hist;
	for (int i = 2; i*i < N; i++) {
		sum += i*i;
		long tmp = sum;
		for (int j = 0; j < i-1; j++) {
			sum -= j*j;
			if (sum < N && isPal(sum)) {
				//cout << j+1 << " " << i << " " << sum << endl;
				hist.insert(sum);
			}
		}
		sum = tmp;
	}

	long ans = 0;
	for (set<long>::iterator it = hist.begin(); it != hist.end(); it++) {
		ans += *it;
	}
	return ans;
}


int main() {
	auto start_t = chrono::high_resolution_clock::now();
	auto ans = process(100000000);
	auto stop_t = chrono::high_resolution_clock::now();
	auto prx_t = chrono::duration_cast<chrono::milliseconds>(stop_t - start_t);
	cout << "Answer: " << ans << " - "
		<< "Processing time: " << prx_t.count() << "ms" << endl;

	return 0;
}
