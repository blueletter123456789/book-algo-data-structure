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
	m := NumStdin()
	a := make([]float64, n)
	for i := 0; i < n; i++ {
		a[i] = float64(NumStdin())
	}

	f := make([][]float64, n+1)
	for i := 0; i <= n; i++ {
		f[i] = make([]float64, n+1)
	}

	for i := 1; i <= n; i++ {
		for j := 0; j < i; j++ {
			sum := 0.0
			for k := j; k < i; k++ {
				sum += a[k]
			}
			f[j][i] = sum / float64(i - j)
		}
	}

	dp := make([][]float64, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = make([]float64, m+1)
		for j := 0; j <= m; j++ {
			dp[i][j] = -math.MaxFloat64
		}
	}
	dp[0][0] = 0
	
	for i := 0; i <= n; i++ {
		for j := 0; j < i; j++ {
			for k := 1; k <= m; k++ {
				// i個目までをkに分割したとき、
				// k-1まで分割して[j, i)の区間が存在したときの平均値の総和
				chmax(&dp[i][k], dp[j][k-1] + f[j][i])
			}
		}
	}

	res := -math.MaxFloat64
	// 区間の数をM個以下にした時の最大値
	for i := 0; i <= m; i++ {
		chmax(&res, dp[n][i])
	}

	for _, row := range dp {
		fmt.Println(row)
	}
	fmt.Println(res)
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}

func chmax(a *float64, b float64) {
	if *a < b {
		*a = b
	}
}

// func main() {
// 	n := NumStdin()
// 	m := NumStdin()
// 	a := make([]float64, n+1)
// 	for i := 1; i <= n; i++ {
// 		a[i] = float64(NumStdin())
// 	}

// 	c := make([][]float64, n)
// 	for i := 0; i < n; i++ {
// 		c[i] = make([]float64, n)
// 		c[i][i] = a[i+1]
// 	}

// 	for i := 0; i < n; i++ {
// 		for j := i+1; j < n; j++ {
// 			avg := 0.0
// 			for k := i; k <= j; k++ {
// 				avg += a[k+1]
// 			}
			
// 			c[i][j] = avg / float64(j - i + 1)
// 		}
// 	}

// 	dp := make([][]float64, m+1)
// 	for i := 0; i <= m; i++ {
// 		dp[i] = make([]float64, n+1)
// 	}

// 	for k := 0; k < m; k++ {
// 		for i := 0; i < n; i++ {
// 			for j := i; j < n; j++ {
// 				// 区間の初期値
// 				chmax(&dp[k+1][j+1], dp[k][j+1])

// 				// k-1分割した数から最大値を取得
// 				chmax(&dp[k+1][j+1], dp[k][i] + c[i][j])
// 			}
// 		}
// 	}

// 	for _, row := range c {
// 		fmt.Println(row)
// 	}
// 	fmt.Println()
// 	for _, row := range dp {
// 		fmt.Println(row)
// 	}
// 	fmt.Println(dp[m][n])
// }
