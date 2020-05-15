package main

import (
	"flag"
	"fmt"
	"github.com/tealeg/xlsx"
	"runtime"
	"time"
)

func main() {
	fileName := *flag.String("f", "data/small.xlsx", "要测试的文件")
	now := time.Now()
	file, _ := xlsx.OpenFile(fileName)
	openSeconds := time.Now().Sub(now).String()
	for _, row := range file.Sheets[0].Rows {
		fmt.Println(row.Cells[0].Value)
	}

	fmt.Println(openSeconds, time.Now().Sub(now).String())
	ms := &runtime.MemStats{}
	runtime.ReadMemStats(ms)
	fmt.Println("Used Memory:", ms.Alloc/1024/1024)
}
