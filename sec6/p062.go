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
	a := make([]int, n)
	for i := range a {
		a[i] = NumStdin()
	}
	b := make([]int, n)
	for i := range b {
		b[i] = NumStdin()
	}
	c := make([]int, n)
	for i := range c {
		c[i] = NumStdin()
	}

	sort.Slice(a, func(i, j int) bool { return a[i] < a[j] })
	sort.Slice(c, func(i, j int) bool { return c[i] < c[j] })

	var ans int
	for _, num := range b {
		idxA := sort.SearchInts(a, num)
		idxC := upperBound(c, num)
		ans += idxA * (n - idxC)
	}

	fmt.Println(ans)
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
