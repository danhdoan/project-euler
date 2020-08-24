fn main() {
    let mut curr = 0;
    let mut cnt = 1;
    let ans = loop {
        curr += cnt;
        if num_divisor(curr) > 500 {
            break curr;
        }
        cnt += 1;
    };

    println!("Answer: {}", ans);
}

fn num_divisor(x: i32) -> i32 {
    let mut ans = if x != 1 {2} else {1};

    let mut i: i32 = 2;
    while i*i <= x {
        if x % i == 0 {
            ans += 1;
            if i*i != x {
                ans += 1;
            }
        }
        i += 1;
    }

    return ans;
}
