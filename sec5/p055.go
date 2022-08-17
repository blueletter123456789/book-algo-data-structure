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

	a := make([]int, n)
	for i := 0; i < n; i++ {
		a[i] = NumStdin()
	}

	dp := make([]bool, w+1)
	dp[0] = true
	for i := 0; i < n; i++ {
		for j := 0; j <= w; j++ {
			if a[i] <= j {
				dp[j] = dp[j] || dp[j-a[i]]
			}
		}
	}

	if dp[w] {
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
