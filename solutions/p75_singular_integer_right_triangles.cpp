#include <iostream>
#include <chrono>
#include <cmath>
#include <vector>
using namespace std;

int gcd(int a, int b) {
	return b ? gcd(b, a % b) : a;
}

int process(int N) {
	vector<int> cnt(N+1, 0);
	for (int m = 2; m*m <= N/2; m++) {
		for (int n = 1; n < m; n++) {
			if ((m+n) % 2 == 0 || gcd(m, n) != 1) 
				continue;

			int a = m*m - n*n,
				b = 2*m*n,
				c = m*m + n*n,
				p = a + b + c;
			while (p <= N) {
				cnt[p]++;
				p += a + b + c;
			}
		}
	}

	int ans = 0;
	for (int i = 12; i <= N; i++)
		ans += cnt[i] == 1;
	
	return ans;
}


int main() {
	auto start_t = chrono::high_resolution_clock::now();
	int ans = process(1500000);
	auto stop_t = chrono::high_resolution_clock::now();
	auto prx_t = chrono::duration_cast<chrono::milliseconds>(stop_t - start_t);
	cout << "Answer: " << ans 
		<< " Processing time: " << prx_t.count() << "ms" << endl;

	return 0;
}
