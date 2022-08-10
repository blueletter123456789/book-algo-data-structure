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

	ans := 0
	for i := 0; i < (1 << (len(n)-1)); i++ {
		sum := 0
		add := string(n[0])
		for j := 0; j < len(n)-1; j++ {
			if (i & (1 << j)) != 0 {
				sum += convAtoi(add)
				add = string(n[j+1])
			} else {
				add = add + string(n[j+1])
			}
		}
		sum += convAtoi(add)
		ans += sum
	}

	fmt.Println(ans)
}

func NumStdin() string {
	scan.Scan()
	return scan.Text()
}

func convAtoi(a string) int {
	x, err := strconv.Atoi(a)
	if err != nil {
		panic(err)
	}
	return x
}
