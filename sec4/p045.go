package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var scan = bufio.NewScanner(os.Stdin)

const (
	initBufSize = 10000
	maxBufSize = 10000000
)

func init() {
	buf := make([]byte, initBufSize)
	scan.Buffer(buf, maxBufSize)
	scan.Split(bufio.ScanWords)
}

func main() {
	n := NumStdin()

	seen := make(map[int]bool, 1 << 15)

	fmt.Println(calc(0, n, seen))
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}

func calc(x, n int, seen map[int]bool) int {

	if x > n {
		return 0
	}
	
	res := 0
	if is753(x){
		res = 1
	}

	num3 := x*10 + 3
	num5 := x*10 + 5
	num7 := x*10 + 7

	if is_seen, ok := seen[num3]; !is_seen || !ok {
		seen[num3] = true
		res += calc(num3, n, seen)
	}

	if is_seen, ok := seen[num5]; !is_seen || !ok {
		seen[num5] = true
		res += calc(num5, n, seen)
	}

	if is_seen, ok := seen[num7]; !is_seen || !ok {
		seen[num7] = true
		res += calc(num7, n, seen)
	}

	return res
}

func is753(x int) bool {
	cnt := make(map[int]bool, 3)
	cnt[3] = false
	cnt[5] = false
	cnt[7] = false

	for x > 0 {
		a := x % 10
		if is_seen, ok := cnt[a]; ok && !is_seen {
			cnt[a] = true
		}
		x /= 10
	}

	return cnt[3] && cnt[5] && cnt[7]
}


// Sample code
// func main() {
// 	n := NumStdin()
// 	counter := 0

// 	calc(n, 0, 0, &counter)

// 	fmt.Println(counter)
// }

// func NumStdin() int {
// 	scan.Scan()
// 	num, err := strconv.Atoi(scan.Text())
// 	if err != nil {
// 		panic(err)
// 	}
// 	return num
// }

// func calc(n, cur, use int, counter *int) {
// 	if cur > n {
// 		return
// 	}

// 	if use == 0b111 {
// 		*counter++
// 	}

// 	calc(n, cur*10 + 7, use | 0b001, counter)

// 	calc(n, cur*10 + 5, use | 0b010, counter)

// 	calc(n, cur*10 + 3, use | 0b100, counter)
// }
