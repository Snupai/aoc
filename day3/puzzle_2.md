## --- Part Two ---

The escalator doesn't move. The Elf explains that it probably needs more joltage to overcome the [static friction](https://en.wikipedia.org/wiki/Static_friction) of the system and hits the big red "joltage limit safety override" button. You lose count of the number of times she needs to confirm "yes, I'm sure" and decorate the lobby a bit while you wait.

Now, you need to make the largest joltage by turning on **exactly twelve** batteries within each bank.

The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; the only difference is that now there will be `12` digits in each bank's joltage output instead of two.

Consider again the example from before:
```
987654321111111
811111111111119
234234234234278
818181911112111
```
Now, the joltages are much larger:

- In <code><span style="font-weight:bold">987654321111</span>111</code>, the largest joltage can be found by turning on everything except some `1`s at the end to produce **`987654321111`**.
- In the digit sequence <code><span style="font-weight:bold">81111111111</span>111<span style="font-weight:bold">9</span></code>, the largest joltage can be found by turning on everything except some `1`s, producing **`811111111119`**.
- In <code>23<span style="font-weight:bold">4</span>2<span style="font-weight:bold">34234234278</span></code>, the largest joltage can be found by turning on everything except a `2` battery, a `3` battery, and another `2` battery near the start to produce **`434234234278`**.
- In <code><span style="font-weight:bold">8</span>1<span style="font-weight:bold">8</span>1<span style="font-weight:bold">8</span>1<span style="font-weight:bold">911112111</span></code>, the joltage **`888911112111`** is produced by turning on everything except some `1`s near the front.

The total output joltage is now much larger: `987654321111` + `811111111119` + `434234234278` + `888911112111` = **`3121910778619`**.

**What is the new total output joltage?**