fn main() {
    const MAXN: usize = 2_000_000;
    let mut sieve: Vec<bool> = vec![true; MAXN];

    for i in 2..MAXN/2 {
        let mut j = 2*i;
        while j < MAXN {
            sieve[j] = false;
            j += i;
        }
    }

    let mut ans = 0;
    for i in 2..MAXN {
        ans += if sieve[i] {i} else {0};
    }

    println!("Answer: {}", ans);
}
