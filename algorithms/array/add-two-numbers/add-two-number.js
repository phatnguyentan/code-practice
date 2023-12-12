/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

function addTwoNumbers(l1, l2) {
    let result = new ListNode();
    let startResult = new ListNode();
    startResult.next = result;
    let startL1 = new ListNode();
    startL1.next = l1;
    let startL2 = new ListNode();
    startL2.next = l2;
    // find l1 length
    const l1Length = countList(l1);

    // find l2 length
    const l2Length = countList(l2);

    // find difference length
    let diff = Math.abs(l1Length - l2Length);
    if (l1Length > l2Length) {
        addTwoNumbersByOrder(startL1.next, startL2.next, diff);
    } else {
        addTwoNumbersByOrder(startL2.next, startL1.next, diff);
    }

    // travel difference length of bigger length
    function addTwoNumbersByOrder(l1, l2, diff) {
        function recursive(l1, l2) {
            let mem = 0;
            // add 2 numbers
            if (l1.next && l2.next) {
                mem = recursive(l1.next, l2.next);
                result.next = new ListNode();
                result = result.next;
            }
            let sum = l1.val + l2.val + mem;
            mem = Math.floor(sum / 10);
            result.val = sum % 10;
            return mem;
        }
        let startL1 = new ListNode();
        startL1.next = l1;
        for (let i = 0; i < diff; i++) {
            l1 = l1.next;
        }
        let mem = recursive(l1, l2);
        l1 = startL1.next;
        for (let i = 0; i < diff; i++) {
            result.next = new ListNode();
            result = result.next;
            let sum = l1.val + result.val + mem;
            mem = Math.floor(sum / 10);
            result.val = sum % 10;
            l1 = l1.next;
        }
        if(mem == 1) {
            result.next = new ListNode(1);
        }
    }

    // travel rest
    function countList(l) {
        let count = 0;
        while (l && l.val !== null) {
            l = l.next;
            count = count + 1;
        }
        return count;
    }
    return startResult.next;
}
function test() {
    let node1 = new ListNode(null, null);
    let start1 = new ListNode(null, null);
    start1.next = node1;
    [2, 4, 3].forEach((num) => {
        node1.val = num;
        node1.next = new ListNode(null, null);
        node1 = node1.next;
    });
    let node2 = new ListNode(null, null);
    let start2 = new ListNode(null, null);
    start2.next = node2;
    [5, 6, 4].forEach(num => {
        node2.val = num;
        node2.next = new ListNode(null, null);
        node2 = node2.next;
    });
    console.log(addTwoNumbers(start1.next, start2.next));
}
test();



// console.log(addTwoNumbers(node1, node2));
// console.log(addTwoNumbers([0], [0]));
// console.log(addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]));