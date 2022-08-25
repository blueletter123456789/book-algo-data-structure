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
	m := NumStdin()
	p := make([]int, n)
	for i := range p {
		p[i] = NumStdin()
	}
	p = append(p, 0)

	pair := make([]int, 0, (n+1)*(n+1))
	seen := make(map[int]struct{}, (n+1)*(n+1))
	for _, val1 := range p {
		for _, val2 := range p {
			num := val1 + val2
			if _, ok := seen[num]; ok {
				continue
			}
			pair = append(pair, num)
			seen[num] = struct{}{}
		}
	}

	sort.Slice(pair, func(i, j int) bool { return pair[i] < pair[j] })

	ans := 0
	for _, val := range pair {
		tgt := m - val
		idx := max(0, sort.SearchInts(pair, tgt)-1)
		score := val + pair[idx]
		if score <= m && score > ans {
			ans = score
		}
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

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
