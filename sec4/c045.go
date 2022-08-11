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

	fmt.Println(fibo(n))
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}

func fibo(n int) int {
	
	fmt.Printf("fibo(%d) is called\n", n)

	if n == 0 {
		return 0
	}
	if n == 1 {
		return 1
	}

	// return fibo(n-1) + fibo(n-2)

	result := fibo(n-1) + fibo(n-2)
	fmt.Printf("fibo(%d)'s answer is %d\n", n, result)
	return result
}
