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
	lst := make([]int, n)
	for i := 0; i < n; i++ {
		lst[i] = NumStdin()
	}

	minVal := (1 << 63) - 1
	for _, val := range lst {
		if minVal > val {
			minVal = val
		}
	}

	fmt.Println(minVal)
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}
