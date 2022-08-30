package main

import (
	"bufio"
	"fmt"
	"math"
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
	a := float64(NumStdin())
	b := float64(NumStdin())
	c := float64(NumStdin())

	calc := func (t float64) float64 {
		return a*t + b*math.Sin(c*t*math.Pi)
	}
	
	left, right := 0.0, math.Pow10(9)
	for i := 0; i < 100; i++ {
		mid := (left + right) / 2
		ret := calc(mid)
		if ret >= 100 {
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
