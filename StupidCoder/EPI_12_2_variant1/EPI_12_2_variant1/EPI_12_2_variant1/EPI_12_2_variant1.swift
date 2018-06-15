//
//  EPI_12_2_variant1.swift
//  EPI_12_2_variant1
//
//  Created by Qingchuan Zhu on 6/15/18.
//  Copyright © 2018 Qingchuan Zhu. All rights reserved.
//

import Foundation

class Solution {
    func intervalEncloseK(_ array:[Int], target:Int) -> (Int, Int) {
        var interval = (L: -1, U: -1)
        
        let low = lowBundarySearch(array, target: target)
        let high = highBoundaySearch(array, target: target)
        
        if high == -1 {
            // target larger than or equal to the last element
            if low != array.count - 1{
                interval = (L: low+1, U: array.count - 1)
            }
        }
        
        if low == -1 {
            // target smaller or equal to the first element
            if high != 0 {
                interval = (L: 0, U: high - 1)
            }
        }
        
        if low != -1 && high != -1 && low != high - 1 {
            interval = (L: low+1, U: high-1)
        }
        
        return interval
    }
    
    private func lowBundarySearch(_ array:[Int], target:Int) -> Int {
        // find last element smaller than target
        var lowBound:Int = -1
        
        var low = 0
        var high = array.count - 1
        while low <= high {
            let mid = low + (high - low) / 2
            if array[mid] < target {
                lowBound = mid
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        return lowBound
    }
    
    private func highBoundaySearch(_ array:[Int], target:Int) -> Int {
        // find first element larger than target
        var highBound:Int = -1
        
        var low = 0
        var high = array.count - 1
        while low <= high {
            let mid = low + (high - low) / 2
            if array[mid] <= target {
                low = mid + 1
            } else {
                high = mid - 1
                highBound = mid
            }
        }
        return highBound
    }
}
