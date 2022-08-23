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

	var cnt int
	left, right := 20, 36
	for right >= left {
		mid := (left + right) / 2

		fmt.Printf("left:%d, mid:%d, right:%d\n", left, mid, right)

		if mid == n {
			fmt.Printf("The answer is %d\n", mid)
			fmt.Println(cnt <= 4, cnt)
			break
		} else if mid > n {
			right = mid - 1
		} else {
			left = mid + 1
		}
		cnt++
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

