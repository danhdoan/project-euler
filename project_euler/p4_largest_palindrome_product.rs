fn is_pal(s: String) -> bool {
    let v: Vec<_> = s.chars().collect();
    let n: usize = v.len();
    for i in 0..n/2 {
        if v[i] != v[n - i - 1] {
            return false;
        }
    }

    true
}

fn main() {
    let mut ans = -1;
    for x in 100..1000 {
        for y in 100..1000 {
            let z = x * y;
            if is_pal(z.to_string()) && ans < z {
                ans = z;
            }
        }
    }
    println!("Answer: {}", ans);
}
