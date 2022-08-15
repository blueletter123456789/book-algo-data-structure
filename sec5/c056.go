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

var n int
var h, dp []int

func main() {
	n = NumStdin()
	h = make([]int, n)
	dp = make([]int, n)
	for i := 0; i < n; i++ {
		h[i] = NumStdin()
		dp[i] = math.MaxInt64
	}
	
	fmt.Println(rec(n-1))
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}

func rec(i int) int {
	if i == 0 {
		return 0
	}

	if dp[i] < math.MaxInt64 {
		return dp[i]
	}

	res := math.MaxInt64

	chmin(&res, rec(i-1) + abs(h[i] - h[i-1]))

	if i > 1 {
		chmin(&res, rec(i-2) + abs(h[i] - h[i-2]))
	}

	dp[i] = res
	return res
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
