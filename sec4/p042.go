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

	memo := make([]int, n+1)
	for i := 0; i <= n; i++ {
		memo[i] = -1
	}

	fmt.Println(tribo(n, memo))

}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}

func tribo(i int, memo []int) int {
	if i <= 1 {
		return 0
	}
	if i == 2 {
		return 1
	}

	// Code when not using memo (4.1)
	// return tribo(i-1) + tribo(i-2) + tribo(i-3)

	if memo[i] >= 0 {
		return memo[i]
	}

	memo[i] = tribo(i-1, memo) + tribo(i-2, memo) + tribo(i-3, memo)

	return memo[i]
}
