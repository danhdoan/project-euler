fn main() {
    const MOD: u64 = 10_000_000_000;
    let mut ans = 0;

    for i in 1..1001 {
        let val = self_power(i, MOD);
        ans = (ans + val) % MOD;
    }

    println!("Answer: {}", ans);
}

fn self_power(x: u64, modul: u64) -> u64 {
    let mut ans: u64 = 1;
    for _i in 0..x {
        ans = (ans * x) % modul;
    }
    return ans;
}
