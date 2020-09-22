#include <iostream>
#include <chrono>
#include <cmath>
#include <vector>
#include <set>
using namespace std;

vector<int> generatePrimes(int N) {
	vector<bool> sieve(N + 1, true);
	for (int i = 2; i <= N / 2; i++) {
		if (!sieve[i]) continue;
		for (int j = 2*i; j <= N; j += i)
			sieve[j] = false;
	}

	vector<int> primes;
	for (int i = 2; i < sieve.size(); i++) {
		if (sieve[i])
			primes.push_back(i);
	}

	return primes;
}


int M(int p, int q, int N) {
	long lim1 = 0, tmp = 1;
	while (tmp <= N) {
		lim1 += 1;
		tmp *= p;
	}

	long lim2 = 0;
	tmp = 1;
	while (tmp <= N) {
		lim2 += 1;
		tmp *= q;
	}

	int ans = 0;
	for (int i = 1; i < lim1; i++) {
		for (int j = 1; j < lim2; j++) {
			long prod = (long)(pow(p, i)) * (long)(pow(q, j));
			if (prod <= N) {
				ans = max(ans, (int)prod);
			}
			else break;
		}
	}
	return ans;
}

long process(int N) {
	vector<int> primes = generatePrimes(N / 2);

	set<int> hist;
	for (int i = 0; i < primes.size(); i++) {
		int p = primes[i];
		if ((long)p * p > N) break;

		for (int j = i+1; j < primes.size(); j++) {
			int q = primes[j];
			if ((long)p * q > N) break;

			int mx_prod = M(p, q, N);
			hist.insert(mx_prod);
		}
	}

	long ans = 0;
	for (set<int>::iterator it = hist.begin(); it != hist.end(); it++) {
		ans += *it;
	}

	return ans;
}


int main() {
	int N = 10000000;

	auto start_t = chrono::high_resolution_clock::now();
	auto ans = process(N);
	auto stop_t = chrono::high_resolution_clock::now();
	auto prx_t = chrono::duration_cast<chrono::milliseconds>(stop_t - start_t);
	cout << "Answer: " << ans 
		<< " Processing time: " << prx_t.count() << "ms" << endl;

	return 0;
}
