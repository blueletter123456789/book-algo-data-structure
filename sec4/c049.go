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

	if partSum(n, w, a) {
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


func partSum(i, w int, a []int) bool {
	if i == 0 {
		return w == 0
	}

	// a[i]を選ばないケース
	if partSum(i-1, w, a) {
		return true
	}

	// a[i]を選ぶケース
	if partSum(i-1, w-a[i-1], a) {
		fmt.Println(i, a[i-1], w)
		return true
	}

	return false
}
