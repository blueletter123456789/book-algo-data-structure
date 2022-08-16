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
	a := make([]int, n)
	b := make([]int, n)
	c := make([]int, n)

	for i := 0; i < n; i++ {
		a[i] = NumStdin()
		b[i] = NumStdin()
		c[i] = NumStdin()
	}

	dpA := make([]int, n+1)
	dpB := make([]int, n+1)
	dpC := make([]int, n+1)

	for i := 0; i < n; i++ {
		chmax(&dpA[i+1], dpB[i] + b[i])
		chmax(&dpA[i+1], dpC[i] + c[i])

		chmax(&dpB[i+1], dpA[i] + a[i])
		chmax(&dpB[i+1], dpC[i] + c[i])

		chmax(&dpC[i+1], dpA[i] + a[i])
		chmax(&dpC[i+1], dpB[i] + b[i])
	}

	fmt.Println(max(dpA[n], max(dpB[n], dpC[n])))
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

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
