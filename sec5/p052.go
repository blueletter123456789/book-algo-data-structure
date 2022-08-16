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
	w := NumStdin()

	a := make([]int, n+1)
	for i := 0; i < n; i++ {
		a[i] = NumStdin()
	}

	dp := make([][]bool, n+1)
	dp[0] = make([]bool, w+1)
	dp[0][0] = true

	for i := 0; i < n; i++ {
		dp[i+1] = make([]bool, w+1)
		for j := 0; j <= w; j++ {
			dp[i+1][j] = dp[i][j]

			if a[i] > j {
				continue
			}

			dp[i+1][j] = dp[i+1][j] || dp[i][j-a[i]]
		}
	}

	if dp[n][w] {
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
