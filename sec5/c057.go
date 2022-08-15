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

	wei := make([]int, n)
	val := make([]int, n)
	for i := 0; i < n; i++ {
		wei[i] = NumStdin()
		val[i] = NumStdin()
	}

	dp := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = make([]int, w+1)
	}

	for i := 0; i < n; i++ {
		for j := 0; j <= w; j++ {
			// 品物を選ぶ方法
			if wei[i] <= j {
				chmax(&dp[i+1][j], dp[i][j-wei[i]] + val[i])
			}

			// 品物を選ばない方法
			chmax(&dp[i+1][j], dp[i][j])
		}
	}

	fmt.Println(dp[n][w])
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}

func chmax(a *int, b int) {
	if *a < b {
		*a = b
	}
}
