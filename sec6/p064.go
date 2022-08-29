package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
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
	c := NumStdin()
	x := make([]int, n)
	for i := range x {
		x[i] = NumStdin()
	}

	sort.Slice(x, func(i, j int) bool { return x[i] < x[j] })

	left, right := 0, 1_000_000_000
	for right - left > 1 {
		mid := (left + right) / 2
		cnt := selectStoles(x, mid)
		// fmt.Println(left, mid, right, cnt)
		if cnt >= c {
			left = mid
		} else {
			right = mid
		}
	}

	fmt.Println(left)
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}

func selectStoles(x []int, dist int) int {
	cnt := 1
	var prev int

	for i := 0; i < len(x); i++ {
		if x[i] - x[prev] >= dist {
			cnt++
			prev = i
		}
	}

	return cnt
}
