package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
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
	s := stdin()
	t := stdin()
	lenS := len(s)
	lenT := len(t)

	dp := make([][]int, lenS+1)
	for i := 0; i <= lenS; i++ {
		dp[i] = make([]int, lenT+1)
		for j := 0; j <= lenT; j++ {
			dp[i][j] = math.MaxInt64
		}
	}
	dp[0][0] = 0

	for i := 0; i <= lenS; i++ {
		for j := 0; j <= lenT; j++ {
			// Sの文字を変更
			if i > 0 && j > 0 {
				if string(s[i-1]) == string(t[j-1]) {
					chmin(&dp[i][j], dp[i-1][j-1])
				} else {
					chmin(&dp[i][j], dp[i-1][j-1] + 1)
				}
			}

			// Sに文字を挿入
			if j > 0 {
				chmin(&dp[i][j], dp[i][j-1]+1)
			}

			// Sの文字を削除
			if i > 0 {
				chmin(&dp[i][j], dp[i-1][j]+1)
			}
		}
	}

	fmt.Println(dp[lenS][lenT])
}

func stdin() string {
	scan.Scan()
	return scan.Text()
}

func chmin(a *int, b int) {
	if *a > b {
		*a = b
	}
}
