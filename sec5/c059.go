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
	c := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		c[i] = make([]int, n+1)
		for j := 0; j <= n; j++ {
			c[i][j] = NumStdin()
		}
	}

	dp := make([]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = math.MaxInt64
	}
	dp[0] = 0

	for i := 0; i <= n; i++ {
		for j := 0; j < i; j++ {
			chmin(&dp[i], dp[j] + c[i][j])
		}
	}

	fmt.Println(dp[n])
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
