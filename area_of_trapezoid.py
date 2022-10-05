#!/usr/bin/env python3
# Created by: Cameron Diedrich
# Created on: Sep 2022
# This program calculates the area and perimeter of a trapeziod
# with side length inputted from the user

def main():
# this function calculates area 

    # input
    length1 = int(input("Enter length of top side of trapeziod (mm): "))
    length2 = int(input("Enter length of bottom side of trapeziod (mm): "))
    height = int(input("Enter height of the trapeziod(mm): "))

    # process
    area =(length1+length2) * height /2

    # output
    print("")
    print("Area is {0} mm2.".format(area))

    print("\nDone.")

if __name__ == "__main__":
    main()