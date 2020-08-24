fn main() {
    let mut sum_sqr = 0;
    let mut sum = 0;

    for i in 1..101 {
        sum_sqr += i*i;
        sum += i;
    }

    let ans  = sum*sum - sum_sqr;
    println!("Answer: {}", ans);
}
