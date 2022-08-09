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
	INF = (1 << 63) - 1
)

func init() {
	buf := make([]byte, initBufSize)
	scan.Buffer(buf, maxBufSize)
	scan.Split(bufio.ScanWords)
}

func main() {
	n := NumStdin()
	maxNum, minNum := -1, INF

	for i := 0; i < n; i++ {
		x := NumStdin()
		if maxNum < x {
			maxNum = x
		}
		if minNum > x {
			minNum = x
		}
	}

	fmt.Println(maxNum - minNum)
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}
