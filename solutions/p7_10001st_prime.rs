fn main() {
    const MAXN: usize = 110_000;

    let mut sieve: Vec<bool> = vec![true; MAXN];

    for i in 2..MAXN/2 {
        let mut j = 2*i;
        while j < MAXN {
            sieve[j] = false;
            j += i;
        }
    }

    let mut cnt = 0;
    let mut i = 2;
    let ans = loop {
        if sieve[i] {
            cnt += 1;
            if cnt == 10_001 {
                break i;
            }
        }
        i += 1;
    };

    println!("Answer: {}", ans);

}
