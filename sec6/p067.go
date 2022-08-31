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

type BIT struct {
	lst []int
	n int
}

func New(n int) *BIT {
	return &BIT{
		lst: make([]int, n+1),
		n: n,
	}
}

func (bt *BIT) sum(i int) int {
	s := 0
	i++
	for i > 0 {
		s += bt.lst[i]
		i -= (i & -i)
	}
	return s
}

func (bt *BIT) add(i, x int) {
	i++
	for i <= bt.n {
		bt.lst[i] += x
		i += (i & -i)
	}
}

func (bt *BIT) part(i, j int) int {
	return bt.sum(j-1) - bt.sum(i-1)
}

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

	left, right := 0, 1 << 30
	// To assign values less than 0 as well.
	geta := n+1
	for right - left > 1 {
		mid := (left + right) / 2
		var num, sum int
		bt := New(n*2 + 10)
		bt.add(sum+geta, 1)
		for _, val := range a {
			var isUnder int
			if val <= mid {
				isUnder = 1
			} else {
				isUnder = -1
			}
			// Number of items in [1, i) that exceed "mid"
			sum += isUnder
			num += bt.part(1, sum+geta)
			bt.add(sum+geta, 1)
		}

		// fmt.Println(left, mid, right, num)

		if num > (n+1)*n/2/2 {
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
