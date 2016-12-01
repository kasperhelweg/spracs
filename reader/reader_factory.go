package reader

import "errors"

type ReaderFactory func(conf map[string]string) (Reader, error)

func NewReader(readerType, file string) (Reader, error) {

	switch readerType {
	case "list":
		reader := &lReader{file: file}

		return reader.Init(), nil

	case "csv":
		reader := &cReader{file: file}

		return reader.Init(), nil

	default:
		panic(errors.New("unknown reader"))
	}
}
