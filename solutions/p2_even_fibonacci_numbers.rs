fn main() {
    let mut f0 = 1;
    let mut f1 = 2;
    let mut ans = 0;

    while f1 <= 4000_000 {
        if f1 % 2 == 0 {
            ans += f1;
        }

        let f2 = f0 + f1;
        f0 = f1;
        f1 = f2;
    }

    println!("Answer: {}", ans);
}
