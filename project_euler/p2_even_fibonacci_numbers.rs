fn main() {
    let mut f0 = 1;
    let mut f1 = 2;
    let mut ans = 2;

    loop {
        let f2 = f0 + f1;
        if f2 > 4000_000 {
            break;
        }

        if f2 % 2 == 0 {
            ans += f2;
        }

        f0 = f1;
        f1 = f2;
    }

    println!("Answer: {}", ans);
}
