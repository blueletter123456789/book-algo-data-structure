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
	k := NumStdin()
	a := make([]int, n)
	b := make([]int, n)
	for i := 0; i < n; i++ {
		a[i] = NumStdin()
	}
	for i := 0; i < n; i++ {
		b[i] = NumStdin()
	}

	minValue := (1 << 63) - 1
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if a[i] + b[j] < k {
				continue
			}
			if a[i] + b[j] < minValue {
				minValue = a[i] + b[j]
			}
		}
	}

	fmt.Println(minValue)
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}
