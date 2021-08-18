var twoSum = function (nums, target) {
    var indexes = [];

    for (var i = 0; i < nums.length; i++) {
        let j = nums.indexOf(target - nums[i])
        if (j !== -1 && j !== i) {
            indexes.push(i, j)
            break
        }
    }
    return indexes;
}

// console.log(twoSum([1, 2, 3, 4, 5], 9))
console.log(twoSum([3, 2, 4], 6))


var twoSum2 = function (nums, target) {
    var test = [];

    for (var i = 0; i < nums.length; i++) {
        for (var j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target) {
                test.push(i);
                test.push(j);
            }
        }
    }
    return test;
}
