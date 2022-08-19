package main

import (
	"bufio"
	"fmt"
	"math"
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
	w := NumStdin()

	a := make([]int, n)
	m := make([]int, n)
	
	for i := 0; i < n; i++ {
		a[i] = NumStdin()
	}

	for i := 0; i < n; i++ {
		m[i] = NumStdin()
	}

	dp := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = make([]int, w+1)
		for j := 0; j <= w; j++ {
			dp[i][j] = math.MaxInt64
		}
	}
	dp[0][0] = 0

	for i := 0; i < n; i++ {
		for j := 0; j <= w; j++ {

			if dp[i][j] < math.MaxInt64 {
				dp[i+1][j] = 0
			}

			if a[i] > j {
				continue
			}

			// dp[i][j] < math.MaxInt64で条件を満たしているため
			// 該当する条件分岐は必要ない
			// if dp[i][j-a[i]] < math.MaxInt64 {
			// 	chmin(&dp[i+1][j], 1)
			// }

			if dp[i+1][j-a[i]] < math.MaxInt64 && dp[i+1][j-a[i]] < m[i] {
				chmin(&dp[i+1][j], dp[i+1][j-a[i]] + 1)
			}
		}
	}

	if dp[n][w] < math.MaxInt64 {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}

func chmin(a *int, b int) {
	if *a > b {
		*a = b
	}
}
