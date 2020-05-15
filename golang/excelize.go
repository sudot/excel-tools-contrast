package main

import (
	"flag"
	"fmt"
	"github.com/360EntSecGroup-Skylar/excelize"
	"runtime"
	"time"
)

func main() {
	fileName := *flag.String("f", "data/small.xlsx", "要测试的文件")
	now := time.Now()
	file, _ := excelize.OpenFile(fileName)
	openSeconds := time.Now().Sub(now).String()
	sheet := file.WorkBook.Sheets.Sheet[0]
	for _, row := range file.GetRows(sheet.Name) {
		fmt.Println(row[0])
	}

	fmt.Println(openSeconds, time.Now().Sub(now).String())
	ms := &runtime.MemStats{}
	runtime.ReadMemStats(ms)
	fmt.Println("Used Memory:", ms.Alloc/1024/1024)
}
