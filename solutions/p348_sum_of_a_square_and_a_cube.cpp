#include <iostream>
#include <chrono>
#include <map>
#include <vector>
#include <cmath>
using namespace std;

long process() {
	long ans = 0;
	long MAXN = 40000;

	long max_x = 0, max_y = 0;
	map<long, int> hist;
	for (int i = 2; i <= MAXN; i++) {
		for (int j = 2; j <= MAXN; j++) {
			long x = (long)i*i + (long)j*j*j;

			long y = 0, t = x;
			while (t > 0) {
			   y = y*10 + t % 10;
			   t /= 10;
			}
			if (x == y) {
				if (hist.find(x) != hist.end()) 
					hist[x] = hist[x] + 1;
				else 
					hist[x] = 1; 
			}
		}
	}

	for (map<long, int>::iterator it = hist.begin(); it != hist.end(); it++) {
		if (it->second == 4) {
			cout << it->first << " " << it->second << endl;
			ans += it->first;
		}
	}

	return ans;
}


int main() {
	auto start_t = chrono::high_resolution_clock::now();
	long ans = process();
	auto stop_t = chrono::high_resolution_clock::now();
	auto prx_t = chrono::duration_cast<chrono::milliseconds>(stop_t - start_t);
	cout << "Answer: " << ans 
		<< " Processing time: " << prx_t.count() << "ms" << endl;

	return 0;
}
