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
	first, second := INF, INF

	for i := 0; i < n; i++ {
		x := NumStdin()

		if x >= second {
			continue
		}

		if x < first {
			first, second = second, first
			first = x
		} else {
			second = x
		}
	}

	fmt.Println(second)
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}
