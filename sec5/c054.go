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
	dp := make([]int, n)
	for i := 0; i < n; i++ {
		h[i] = NumStdin()
		dp[i] = math.MaxInt64
	}

	dp[0] = 0
	for i := 0; i < n-1; i++ {
		
		chmin(&dp[i+1], dp[i] + abs(h[i+1] - h[i]))
		
		if i+2 < n {
			chmin(&dp[i+2], dp[i] + abs(h[i+2] - h[i]))
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

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func chmin(a *int, b int) {
	if *a > b {
		*a = b
	}
}
