fn main() {
    let mut n: i64 = 600851475143;

    let mut i = 3;
    let mut ans = -1;
    while i*i <= n {
        if n % i == 0 {
            if ans < i {
                ans = i;
            }

            while n % i == 0 {
                n /= i;
            }
        }

        i += 2;
    }

    if n > 1 {
        ans = n;
    }

    println!("Answer: {}", ans);
}
