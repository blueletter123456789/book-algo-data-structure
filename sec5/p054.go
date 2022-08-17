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
	k := NumStdin()

	a := make([]int, n)
	for i := 0; i < n; i++ {
		a[i] = NumStdin()
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
			chmin(&dp[i+1][j], dp[i][j])
			
			if a[i] <= j && dp[i][j-a[i]] < math.MaxInt64 {
				chmin(&dp[i+1][j], dp[i][j-a[i]] + 1)
			}
		}
	}

	if dp[n][w] <= k {
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
