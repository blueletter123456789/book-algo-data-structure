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

// Each Interval
type Inter struct {
	start, end int
}

func init() {
	buf := make([]byte, initBufSize)
	scan.Buffer(buf, maxBufSize)
	scan.Split(bufio.ScanWords)
}

func main() {
	// Interval Scheduling Problem
	n := NumStdin()
	sch := make([]Inter, n)
	for i := range sch {
		s, t := NumStdin(), NumStdin()
		sch[i] = Inter{start: s, end: t}
	}

	// Sort by end of interval.
	sort.Slice(sch, func(i, j int) bool { return sch[i].end < sch[j].end })

	var res, curEnd int
	for _, inter := range sch {
		if inter.start < curEnd {
			continue
		}
		res++
		curEnd = inter.end
	}

	fmt.Println(res)
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}
