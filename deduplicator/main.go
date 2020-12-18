package main

import (
	"bufio"
	"flag"
	"os"

	"github.com/sirupsen/logrus"
)

func init() {
	logrus.SetFormatter(&logrus.JSONFormatter{})
	logrus.SetOutput(os.Stdout)
}

func handle(finPath *string, loOfLine int, hiOfLine int) {
	// TODO
}

func getPrefix(oldPrefix string, str string) int {
	if len(oldPrefix) <= len(str) {
		if oldPrefix[:4] == str[:4] {
			return 0
		}
		return -1
	}
	if oldPrefix[:4] == str[:4] {
		return 1
	}
	return -1
}

func main() {
	finPath := flag.String("i", "", "")
	foutPath := flag.String("o", "", "")
	flag.Parse()
	fin, err := os.Open(*finPath)
	if err != nil {
		logrus.Error("The specified file is not found or unreadable.")
	}
	defer fin.Close()
	fout, _ := os.Create(*foutPath)
	defer fout.Close()
	bufReader := bufio.NewReader(fin)
	bufWriter := bufio.NewWriter(fout)
	currentPrefix, _, err := bufReader.ReadLine()
	if err != nil {
		logrus.Warn("The specified file is empty.")
	}
	for {
		line, _, err := bufReader.ReadLine()
		if err != nil {
			logrus.Info("File reading completed.")
			break
		}
		status := getPrefix(string(currentPrefix), string(line))
		if status == -1 {
			bufWriter.WriteString(string(currentPrefix) + "\n")
		}
		if status != 0 {
			currentPrefix = line
		}
	}
}
