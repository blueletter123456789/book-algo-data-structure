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
	for i := range a {
		a[i], b[i] = NumStdin(), NumStdin()
	}

	var sum int
	for i := range a {
		r := a[i] % b[i]
		if r == 0 {
			continue
		}
		sum += b[i] - r
	}

	fmt.Println(sum)
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}
