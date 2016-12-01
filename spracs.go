package main

import (
	"fmt"
	"github.com/molamil-com/spracs/reader"
	"os"
)

func run(readerType, input string) error {
	reader, err := reader.NewReader(readerType, input)
	if err != nil {
		return err
	}

	fmt.Println("using reader: " + reader.File())
	reader.Read()

	return nil
}

func main() {
	if as := os.Args[1:]; len(as) < 2 {
		fmt.Println("Please specify a parser and a file.")
	} else {
		err := run(as[0], as[1])
		if err != nil {
			fmt.Println(err)
		}
	}
}
