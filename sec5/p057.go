package main

import (
	"bufio"
	"fmt"
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
	}

	for i := 0; i <= lenS; i++ {
		for j := 0; j <= lenT; j++ {
			// 一致する場合は対応する文字列を追加
			if i > 0 && j > 0 && s[i-1] == t[j-1] {
				chmax(&dp[i][j], dp[i-1][j-1]+1)
			}

			// LCS(Xn,Ym-1)とLCS(Xn-1,Ym)の長い方となる
			if i > 0 {
				chmax(&dp[i][j], dp[i-1][j])
			}

			if j > 0 {
				chmax(&dp[i][j], dp[i][j-1])
			}
		}
	}

	// ans := ""
	// トレースバック
	ans := make([]byte, 0, min(len(s), len(t)))
	for i, j := lenS, lenT; i > 0 && j > 0; {
		if dp[i][j] == dp[i-1][j] {
			i--
		} else if dp[i][j] == dp[i][j-1] {
			j--
		} else {
			// ans = string(t[j-1]) + ans
			ans = append(ans, t[j-1])
			i--
			j--
		}
	}

	// fmt.Println(ans)
	lenA := len(ans)
	for i := 0; i < lenA/2; i++ {
		ans[i], ans[lenA-i-1] = ans[lenA-i-1], ans[i]
	}
	fmt.Println(string(ans))
}

func stdin() string {
	scan.Scan()
	return scan.Text()
}

func chmax(a *int, b int) {
	if *a < b {
		*a = b
	}
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}
