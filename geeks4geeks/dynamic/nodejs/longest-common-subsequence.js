// function common(arr1, arr2, len1, len2) {
//   if(len1 == 0 || len2 == 0) return 0;
//   if (arr1[len1] == arr2[len2]) return 1 + common(arr1, arr2, len1 -1, len2 -1);
//   if (arr1[len1] != arr2[len2]) return Math.max(common(arr1, arr2, len1 -1, len2), common(arr1, arr2, len1, len2 -1));
// }
function common(arr1, arr2, len1, len2) {
  if(len1 == 0 || len2 == 0) return 0;
  if (arr1[len1] == arr2[len2]) return 1 + common(arr1, arr2, len1 -1, len2 -1);
  if (arr1[len1] != arr2[len2]) return Math.max(common(arr1, arr2, len1 -1, len2), common(arr1, arr2, len1, len2 -1));
}
let str1 = "ABCDGH";
let str2 = "AEDFHR";
console.log(common(str1, str2, str1.length, str2.length));
