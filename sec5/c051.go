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
	h := make([]int, n)
	for i := 0; i < n; i++ {
		h[i] = NumStdin()
	}

	dp := make([]int, n)
	dp[1] = abs(h[1] - h[0])
	for i := 2; i < n; i++ {
		dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]), 
					dp[i-2] + abs(h[i] - h[i-2]))
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

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}
