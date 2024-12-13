package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var n int
	fmt.Scan(&n)

	r := solve(n)
	println(strings.Join(r, " "))

}

func solve(n int) []string {
	res := make([]string, 0, 1_000)

	res = append(res, strconv.FormatInt(int64(n), 10))
	for n != 1 {
		if n%2 == 0 {
			n = n / 2
		} else {
			n = 3*n + 1
		}
		res = append(res, strconv.FormatInt(int64(n), 10))
	}
	return res
}
