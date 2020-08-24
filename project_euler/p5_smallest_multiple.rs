fn main() {
    let mut v = vec![0; 20];

    for mut x in 2..21 {
        let mut i = 2;
        while i*i <= x {
            if x % i == 0 {
                let mut cnt = 0;
                while x % i == 0 {
                    x /= i;
                    cnt += 1;
                }
                if v[i] < cnt {
                    v[i] = cnt;
                }
            }

            i += 1;
        }
        if x > 1 && v[x] == 0 {
            v[x] = 1;
        }
    }

    let mut ans = 1;
    for i in 2..20 {
        while v[i] > 0 {
            ans *= i;
            v[i] -= 1;
        }
    }

    println!("Answer: {}", ans);
}
