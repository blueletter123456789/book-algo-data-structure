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
	a := make([]int, n)
	for i := 0; i < n; i++ {
		a[i] = NumStdin()
	}

	s := make([]int, n+1)
	for i := 0; i < n; i++ {
		s[i+1] = s[i] + a[i]
	}

	dp := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = make([]int, n+1)
		for j := 0; j <= n; j++ {
			if j-i == 1 {
				dp[i][j] = 0
			} else {
				dp[i][j] = math.MaxInt64
			}
		}
	}

	// 合計対象の区間
	for bet := 2; bet <= n; bet++ {
		// 区間の始点
		for i := 0; i+bet <= n; i++ {
			// 区間[i, j)にて１つとなる場合を更新
			j := i + bet

			for k := i+1; k < j; k++ {
				chmin(&dp[i][j], dp[i][k] + dp[k][j] + s[j]-s[i])
			}
		}
	}

	for _, row := range dp {
		fmt.Println(row)
	}
	fmt.Println(dp[0][n])
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
