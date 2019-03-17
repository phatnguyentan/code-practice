

function shortestSubstring(s) {
  let list = [];
  let index = [];
  // Get all characters
  for (let i = 0; i < s.length; i++) {
    if (!index[s[i]]) {
      list.push(s[i]);
      index[s[i]] = true;
    }
  }
  let maxCount = 999999;
  let count = 0;
  let tmp;
  let result;

  for (let i = 0; i <= s.length - (list.length); i++) {
    let j = i;
    let newS = "";
    tmp = [...list];
    // console.log(tmp);

    while (tmp && tmp.length > 0 && s[j]) {
      // console.log(s[j]);
      const index = tmp.indexOf(s[j]);
      if (index != -1) {
        tmp.splice(index, 1);
      } else {
        count = count + 1;
      }
      newS = newS + s[j];
      if (count > maxCount) break;
      j++;
      // console.log("tmp:" + tmp);
    }
    // console.log("j: " + j);
    // console.log("count: " + count);
    // console.log("newS: " + newS);
    // console.log("length: " + newS.length);
    // console.log("tmp: " + tmp);
    if (count < maxCount && tmp.length == 0) {
      maxCount = count;
      result = newS.length;
    }
    newS = "";
    count = 0;
  }
  // Write your code here
  return result;
}

function main(string) {

  const result = shortestSubstring(string);

  console.log(result);

}

// main("bab");
main("aabcce");
// main("dabbcabca");
