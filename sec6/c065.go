package main

import (
	"bufio"
	"fmt"
	"math"
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
	h := make([]int, n)
	s := make([]int, n)
	for i := 0; i < n; i++ {
		h[i] = NumStdin()
		s[i] = NumStdin()
	}

	left, right := 0, math.MaxInt64
	for right - left > 1 {
		mid := (left + right) / 2

		// fmt.Println(left, mid, right)

		ok := true
		t := make([]int, n)
		for i := 0; i < n; i++ {
			if mid < h[i] {
				ok = false
			} else {
				t[i] = (mid - h[i]) / s[i]
			}
		}

		sort.Slice(t, func(i, j int) bool { return t[i] < t[j] })

		for i := 0; i < n; i++ {
			if t[i] < i {
				ok = false
			}
		}

		if ok {
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
