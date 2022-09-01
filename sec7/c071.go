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
	coins := [6]int{500, 100, 50, 10, 5, 1}

	n := NumStdin()
	var a [6]int
	for i := range a {
		a[i] = NumStdin()
	}

	var result [6]int
	for i, num := range coins {
		add := n / num

		if add > a[i] {
			add = a[i]
		}

		n -= num * add
		result[i] = add
	}

	if n > 0 {
		fmt.Println("can't pay.")
		return
	}

	fmt.Println(result)
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}
