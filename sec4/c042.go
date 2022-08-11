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

	fmt.Println(addRecursion(n))
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}

func addRecursion(x int) int {
	fmt.Printf("%d is called\n", x)
	
	if x == 0 {
		return 0
	}

	result := addRecursion(x-1)
	fmt.Printf("%d + %d(func(%d))\n", x, result, x-1)

	return x + result
}
