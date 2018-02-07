// At HackerLand University, a passing grade is any grade 40 points or higher on a 100 point scale. Sam is a professor at the university and likes to round each student’s grade according to the following rules:
//
// If the difference between the grade and the next higher multiple of 5 is less than 3, round to the next higher multiple of 5
// If the grade is less than 38, don’t bother as it’s still a failing grade
// Automate the rounding process then round a list of grades and print the results.
// Sample Input 0
// 4
// 73
// 67
// 38
// 33
// Sample Output 0
// 75
// 67
// 40
// 33

function solve(grades){
    // Complete this function
    return grades.map(g => g = (g%5 > 2 && g >= 38)? g + (5 - g%5) : g );
}
// solve([33, 38, 94, 15])
console.log(solve([33, 38, 94, 15]))
