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
	k := NumStdin()
	a := make([]int, n)
	for i := range a {
		a[i] = NumStdin()
	}
	b := make([]int, n)
	for i := range b {
		b[i] = NumStdin()
	}

	sort.Slice(b, func(i, j int) bool { return b[i] < b[j] })

	check := func (x int) bool {
		var cnt int
		for i := 0; i < n; i++{
			cnt += upperBound(b, x/a[i])
		}

		return cnt >= k
	}

	left, right := 0, 1 << 60
	for right - left > 1 {
		mid := (left + right) / 2
		// fmt.Println(left, mid, right)
		if check(mid) {
			right = mid
		} else {
			left = mid
		}
	}

	fmt.Println(right)
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}

func upperBound(a []int, x int) int {
	return sort.Search(len(a), func(i int) bool { return a[i] > x })
}
