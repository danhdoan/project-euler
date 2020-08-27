fn main() {
    let mut curr = 0;
    let mut cnt = 1;
    let ans = loop {
        curr += cnt;
        if num_divisors(curr) > 500 {
            break curr;
        }
        cnt += 1;
    };

    println!("Answer: {}", ans);
}

fn num_divisors(mut x: i32) -> i32 {
    let mut ans = 1;
    let mut i = 2;
    while i*i <= x {
        let mut cnt = 0;
        if x % i == 0 {
            while x % i == 0 {
                cnt += 1;
                x /= i;
            }
            ans *= cnt + 1;
        }
        i += 1;
    }
    ans *= if x > 1 {2} else {1};
    return ans;
}
