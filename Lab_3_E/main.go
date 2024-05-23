package main

import (
	"fmt"
)

type ValueType struct {
	value int
}

// Change of value type
func modify_value(v ValueType) {
	v.value = 100
	fmt.Println("Inside modify_value function:", v.value) // Має вивести: Inside modifyValue function: 100
}

type ReferenceType struct {
	value int
}

// change
func modify_reference(r *ReferenceType) {
	r.value = 100
	fmt.Println("Inside modify_reference function:", r.value) // Має вивести: Inside modifyReference function: 100
}

func main() {
	//value types
	var int_value int
	var float_value float32
	var string_value string
	var bool_value bool
	var byte_value byte
	var rune_value rune

	int_value = 0 // zero jokes about integers. Integers are some very serious numbers.
	// I am a...
	float_value = 3.1415 // oneer in Go
	string_value = "What a splended day, me Lord, aint it?"
	bool_value = false // alarm, it was my clock
	byte_value = 255   // bits gathered together and created a 2^255 number
	rune_value = 'f'   //bomb

	fmt.Println("Integer example: ", int_value)
	fmt.Println("Float example: ", float_value)
	fmt.Println("String example: ", string_value)
	fmt.Println("Bool example: ", bool_value)
	fmt.Println("Byte example: ", byte_value)
	fmt.Println("Rune example: ", rune_value)
	fmt.Println()

	// Для значення типу
	v := ValueType{value: 10}
	modify_value(v)
	fmt.Println("Outside modify_value function:", v.value) // Output: Outside modifyValue function: 10

	// Для посилання типу
	r := &ReferenceType{value: 10}
	modify_reference(r)
	fmt.Println("Outside modify_reference function:", r.value) // Output: Outside modifyReference function: 100

	//wait for input
	fmt.Print("Press the Enter Key to terminate the program")
	fmt.Scanln()
}
