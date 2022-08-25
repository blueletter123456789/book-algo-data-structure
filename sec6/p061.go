// 座標圧縮
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
	a := make([]int, n)
	for i := 0; i < n; i++ {
		a[i] = NumStdin()
	}

	// 前提に相異なるとあるが、他問題では重複となるケースが存在するため
	vals := make([]int, 0, n)
	seen := make(map[int]struct{}, n)
	for _, val := range a {
		if _, ok := seen[val]; !ok {
			vals = append(vals, val)
			seen[val] = struct{}{}
		}
	}

	sort.Slice(vals, func(i, j int) bool { return vals[i] < vals[j] })

	ans := make([]int, n)
	for i, num := range a {
		idx := sort.SearchInts(vals, num)
		ans[i] = idx
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
