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

// グローバル変数を使用した際
// var memo []int

func main() {
	n := NumStdin()

	memo := make([]int, n+1)
	for i := 0; i <= n; i++ {
		memo[i] = -1
	}

	fmt.Println(fibo(n, memo))
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}

func fibo(n int, memo []int) int {

	if n <= 0 {
		return 0
	}
	if n == 1 {
		return 1
	}

	if memo[n] != -1 {
		return memo[n]
	}

	result := fibo(n-1, memo) + fibo(n-2, memo)
	memo[n] = result

	return result
}
