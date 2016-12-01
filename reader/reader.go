package reader

import (
	"encoding/csv"
	"fmt"
	"io"
	"os"
)

type Reader interface {
	Init() Reader
	File() string
	Read() error
}

type lReader struct {
	file string
}

type cReader struct {
	file string
	data []([]string)
}

func (lr *lReader) Init() Reader {
	return lr
}

func (lr *lReader) File() string {
	return lr.file
}

func (lr *lReader) Read() error {
	return nil
}

func (cr *cReader) Init() Reader {
	f, err := os.Open(cr.file)
	if err != nil {
		panic(err)
	}
	defer f.Close()

	r := csv.NewReader(f)
	for {
		row, err := r.Read()
		if err != nil {
			if err == io.EOF {
				break
			}
			panic(err)
		}

		cr.data = append(cr.data, row)
	}

	fmt.Println("DONE")

	return cr
}

func (cr *cReader) File() string {
	return cr.file
}

func (cr *cReader) Read() error {
	for _, entry := range cr.data {
		fmt.Println(entry)
	}

	return nil
}
