fn main() {
    let mut ans = -1;
    let mut found = false;
    for a in 1..334 {
        let max_b = (1000 - a) / 2;
        for b in a+1..max_b {
            let c = 1000 - a - b;

            if a*a + b*b == c*c {
                ans = a * b * c;
                found = true;
                break;
            }
        }
        if found {
            break;
        }
    }

    println!("Answer: {}", ans);
}
