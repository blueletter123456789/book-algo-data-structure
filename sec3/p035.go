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
	lst := make([]int, n)
	for i := 0; i < n; i++ {
		lst[i] = NumStdin()
	}

	flg := false

	for i := 0; i < (1 << n); i++ {
		sum := 0
		for j := 0; j < n; j++ {
			if (i & (1 << j)) != 0 {
				sum += lst[j]
			}
		}

		if sum == w {
			flg = true
			break
		}
	}

	if flg {
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
