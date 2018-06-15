//
//  EPI_12_1.swift
//  EPI_12_1
//
//  Created by Qingchuan Zhu on 6/15/18.
//  Copyright © 2018 Qingchuan Zhu. All rights reserved.
//

import Foundation

class Solution {
    func firstOccurrence(_ array:[Int], key k:Int) -> Int {
        var index:Int = -1
        
        var low:Int = 0
        var high:Int = array.count - 1
        
        while low <= high  {
            let mid = low + (high - low) / 2
            if array[mid] == k {
                high = mid - 1
                index = mid
            } else if array[mid] > k {
                high = mid - 1
            } else {
                low = mid + 1
            }
        }
        
        return index
    }
}


