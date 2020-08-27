fn main() {
    let mut ans = 0;
    for n in 3..1000 {
        if n % 3 == 0 || n % 5 == 0 {
            ans += n;
        }
    }

    println!("Answer: {}", ans);
}
