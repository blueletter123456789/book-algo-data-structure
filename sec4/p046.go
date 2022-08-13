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

	a := make([]int, n)
	for i := 0; i < n; i++ {
		a[i] = NumStdin()
	}

	seen := make([]map[int]bool, n+1)
	for i := 0; i <= n; i++ {
		seen[i] = make(map[int]bool, w)
	}

	if partSum(n, w, a, seen) {
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

func partSum(i, w int, a []int, seen []map[int]bool) bool {
	if i == 0 {
		return w == 0
	}

	if is_seen, ok := seen[i][w]; ok {
		return is_seen
	}

	seen[i][w] = partSum(i-1, w, a, seen)
	if seen[i][w] {
		return seen[i][w]
	}

	seen[i][w] = partSum(i-1, w-a[i-1], a, seen)
	if seen[i][w] {
		return seen[i][w]
	}

	return seen[i][w]
}
