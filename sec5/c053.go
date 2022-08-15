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
	h := make([]int, n)
	for i := 0; i < n; i++ {
		h[i] = NumStdin()
	}
	dp := make([]int, n)
	for i := 0; i < n; i++ {
		dp[i] = math.MaxInt64
	}

	dp[0] = 0
	for i := 1; i < n; i++ {
		chmin(&dp[i], dp[i-1] + abs(h[i] - h[i-1]))
		if i > 1 {
			chmin(&dp[i], dp[i-2] + abs(h[i] - h[i-2]))
		}
	}

	fmt.Println(dp[n-1])
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

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}
