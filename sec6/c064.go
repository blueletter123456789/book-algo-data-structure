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
	b := make([]int, n)

	for i := 0; i < n; i++ {
		a[i] = NumStdin()
	}
	for i := 0; i < n; i++ {
		b[i] = NumStdin()
	}

	sort.Slice(b, func(i, j int) bool {return b[i] < b[j]})

	ans := 1 << 30
	for _, num := range a {
		tgt := k - num
		if tgt < 0 {
			continue
		}

		idx := lowerBound(b, tgt)

		if len(b) == idx {
			continue
		}

		if num + b[idx] >= k {
			ans = min(ans, num + b[idx])
		}
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

func lowerBound(lst []int, x int) int {
	// lst[i] >= xとなる最小のiを返す
	// lst内の最大値でもx未満となる場合、
	// lst範囲外のインデックスを返すが、lst内の最大値を返す場合は
	// right = len(lst)-1とする

	left, right := -1, len(lst)
	for right - left > 1 {
		mid := (left + right) / 2
		if lst[mid] < x {
			left = mid
		} else {
			right = mid
		}
	}
	return right
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}
