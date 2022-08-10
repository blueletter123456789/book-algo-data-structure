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
	k := NumStdin()
	s := NumStdin()

	cnt := 0
	for a := 0; a <= min(k, s); a++ {
		for b := 0; b <= min(k, s); b++ {
			c := s - (a + b)
			if c >= 0 && c <= k{
				cnt++
			}
		}
	}

	fmt.Println(cnt)
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}