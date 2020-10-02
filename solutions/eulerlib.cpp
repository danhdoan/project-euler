#include <vector>
#include "eulerlib.h"

std::vector<int> generatePrimes(int N) {
	int half = N / 2 + 1;
	std::vector<bool> sieve(half, true);
    sieve[0] = false;
    int i = 1;
    while (2*i*i < half) {
        if (sieve[i]) {
            int curr = 3*i + 1;
            while (curr < half) {
                sieve[curr] = false;
                curr += 2*i + 1;
			}
		}
		i++;
	}

	std::vector<int> primes;
	primes.push_back(2);
	for (int i = 3; i <= N; i += 2) {
        if (sieve[i >> 1])
            primes.push_back(i);
	}
    return primes;
}

