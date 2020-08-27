fn main() {
    let mut ans = 1;
    let mut max_length = 1;
    for i in (2..1000_000).rev() {
        let length = func(i);
        if length > max_length {
            max_length = length;
            ans = i;
        }
    }

    println!("Answer: {}", ans);
}

fn func(mut x: u64) -> i32 {
    let mut cnt = 1;
    while x != 1 {
        cnt += 1;
        x = if x % 2 == 0 {x / 2} else {3*x + 1};
    }
    cnt
}
