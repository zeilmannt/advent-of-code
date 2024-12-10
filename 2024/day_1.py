import numpy as np
import re
import time
from collections import Counter

start_time = time.time()

file_path = '/Users/tomzeilmann/Dev/python/advent-of-code/2024/inputs/input_day_1.txt'

def part_one(time_output: bool):
    left_list, right_list = [], []
    distances = []
    total_distance = 0
    k = 0

    with open(file_path, 'r') as file:
        # Get numbers from input
        for content in file:
            numbers = re.findall(r'^\d+|\d+$', content.strip())
            left_list.append(int(numbers[0]))
            right_list.append(int(numbers[1]))
        
        left_list.sort()
        right_list.sort()
        
        # Calculate all distances    
        for i in range(len(left_list)):
            l, r = left_list[i], right_list[i]
            
            if r > l:
                distances.append(r-l)
            else:
                distances.append(l-r)
                
        # Add all distances to calculate total distance
        for d in distances:
            total_distance += d

                
    end_time = time.time()
    print(f"Total distance: {total_distance}")
    
    if time_output:
        print(f"Execution time: {end_time - start_time:.4f} seconds")

def part_two(time_output: bool):
    left_list, right_list = [], []
    scores = []
    similarity_score = 0
    k = 0

    with open(file_path, 'r') as file:
        # Get numbers from input
        for content in file:
            numbers = re.findall(r'^\d+|\d+$', content.strip())
            left_list.append(int(numbers[0]))
            right_list.append(int(numbers[1]))
        
        left_list.sort()
        right_dict = dict(Counter(right_list))
        
        # Calculate all distances    
        for l in left_list:           
            r = right_dict.get(l)
            if r is None:
                scores.append(0)
            else:
                scores.append(l * r)
                
        # Add all scores to calculate similarity score
        for s in scores:
            similarity_score += s

                
    end_time = time.time()
    print(f"Similarity score: {similarity_score}")
    
    if time_output:
        print(f"Execution time: {end_time - start_time:.4f} seconds")
    
part_two(True)