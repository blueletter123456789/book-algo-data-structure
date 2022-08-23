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
	// n := NumStdin()
	// a := make([]int, n)
	// for i := 0; i < n; i++ {
	// 	a[i] = NumStdin()
	// }

	a := []int{3, 5, 8, 10, 14, 17, 21, 39}

	fmt.Println(binarySearch(a, 10))
	fmt.Println(binarySearch(a, 3))
	fmt.Println(binarySearch(a, 39))

	fmt.Println(binarySearch(a, -100))
	fmt.Println(binarySearch(a, 9))
	fmt.Println(binarySearch(a, 100))
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}

func binarySearch(tgt []int, x int) int {
	left, right := 0, len(tgt)-1
	
	for left <= right {
		mid := (left + right) / 2
		if tgt[mid] == x {
			return mid
		} else if tgt[mid] > x {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}

	return -1
}
